from back_end.repositorio.modelo.farmacia_modelo import Farmacia
from back_end.repositorio.classe_repositorio import Repositorio


class PharmacyRepository(Repositorio):
    """Manages functionalities related to PHARMACY, retrieving and manipulating data from the database"""

    def __init__(self):
        super().__init__()

    def return_instances(self) -> list:
        """Create a list of objects of type Pharmacy; it could be empty if the database has no instances"""

        query_pharmacy = 'SELECT * FROM tb_farm_farmacia;'
        self._db.cursor.execute(query_pharmacy)
        result = self._db.cursor.fetchall()
        list_pharmacy = []
        for obj in range(len(result)):
            list_pharmacy.append(Farmacia(result[obj][0], result[obj][1], result[obj]
                             [2], result[obj][3], result[obj][4], result[obj][5], result[obj][6]))
        return list_pharmacy

    def select(self, columns_to_search: list, search_arguments: list, query_operator="=", query_logic=" AND ") -> list:
        """Return a list of objects that satisfy the given arguments. The "columns_to_search" list
        should have the same size as the "search_arguments" list, and there should be a correspondence between them.

        Database columns:
        "char_andar" - change pharmacy floor
        "char_setor" - change pharmacy sector
        "char_resp" - change pharmacy responsible person
        "char_tipo" - change pharmacy type
        """
        query_pharmacy = f'SELECT * FROM tb_farm_farmacia WHERE '
        for select in range(len(columns_to_search)):
            query_pharmacy += columns_to_search[select] + query_operator + \
                """'"""+str(search_arguments[select])+"""'"""
            if len(columns_to_search) > select + 1:
                query_pharmacy += query_logic
        self._db.cursor.execute(query_pharmacy)
        query_result = self._db.cursor.fetchall()
        list_pharmacy_objects = []
        for obj in range(len(query_result)):
            list_pharmacy_objects.append(Pharmacy(query_result[obj][0], query_result[obj][1], query_result[obj]
                                [2], query_result[obj][3], query_result[obj][4], query_result[obj][5], query_result[obj][6]))
        return list_pharmacy_objects

    def return_types(self):
        """Create a list of pharmacy types; it could be empty if the database has no instances"""
        query_pharmacy = 'SELECT * FROM tb_farm_farmacia;'
        self._db.cursor.execute(query_pharmacy)
        query_result = self._db.cursor.fetchall()
        list_pharmacy_types = []
        for obj in range(len(query_result)):
            list_pharmacy_types.append(query_result[obj][4])

        return list_pharmacy_types, query_result

    def add(self, pharmacy_object: Pharmacy):
        """Insert an object of type Pharmacy"""
        query_pharmacy = """INSERT INTO tb_farm_farmacia(
            char_andar, char_setor, char_resp, char_tipo)VALUES(%s,%s,%s,%s)"""
        values_to_search = (str(pharmacy_object.get_floor()), str(pharmacy_object.get_sector()), str(
            pharmacy_object.get_responsible()), str(pharmacy_object.get_type()))
        self._db.cursor.execute(query_pharmacy, values_to_search)
        self._db.connect.commit()

    def update(self, pharmacy_object: Pharmacy, update_arguments: dict):
        """Update an object. To do this, you need to pass a dictionary with the modifications.
        The key is the column in the database, and the value is the new argument.

        Database columns:
        "char_andar" - change pharmacy floor
        "char_setor" - change pharmacy sector
        "char_resp" - change pharmacy responsible person
        "char_tipo" - change pharmacy type
        """
        for idx in update_arguments:
            # Update a Pharmacy object based on each column
            if idx == "char_andar":
                pharmacy_object.set_floor(update_arguments[idx])
            elif idx == "char_setor":
                pharmacy_object.set_sector(update_arguments[idx])
            elif idx == "char_resp":
                pharmacy_object.set_responsible(update_arguments[idx])
            elif idx == "char_tipo":
                pharmacy_object.set_type(update_arguments[idx])

        query_update = """UPDATE tb_farm_farmacia SET char_andar = %s, char_setor = %s,
        char_resp = %s, char_tipo = %s WHERE id_farm = %s"""
        update_values = (pharmacy_object.get_floor(), pharmacy_object.get_sector(
        ), pharmacy_object.get_responsible(), pharmacy_object.get_type(), str(pharmacy_object.get_id_farm()))
        self._db.cursor.execute(query_update, update_values)
        self._db.connect.commit()

    def delete(self, pharmacy_id: int):
        """Delete an object of type Pharmacy, passing a pharmacy id"""
        pharmacy = self.select(["id_farm"], [pharmacy_id])[0]
        if pharmacy:
            pharmacy.set_active_flag()
            delete_pharmacy = """UPDATE tb_farm_farmacia SET bool_ativo = %s, dat_inativo = %s
            WHERE id_farm = %s"""
            delete_values = (pharmacy.get_active_flag(
            ), pharmacy.get_inactive_date(), str(pharmacy.get_id_farm()))
            self._db.cursor.execute(delete_pharmacy, delete_values)
            self._db.connect.commit()
        else:
            return "Pharmacy not found"
