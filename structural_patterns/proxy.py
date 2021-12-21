from abc import ABC, abstractmethod


class AbstractDatabase(ABC):
    @abstractmethod
    def select_query(self) -> str:
        """"""

    @abstractmethod
    def add_index(self) -> str:
        """"""

    @abstractmethod
    def add_join(self) -> str:
        """"""

    @abstractmethod
    def check_db(self) -> str:
        """"""


class PostgreSql(AbstractDatabase):
    def select_query(self) -> str:
        return "slct * from table where db=psql"

    def add_index(self) -> str:
        return "add index field on table"

    def add_join(self) -> str:
        return "slct a,b from table_a join on table_b"

    def check_db(self) -> bool:
        return True


db_map = {"postgres": PostgreSql,
          "mysql": None}


class OrmProxy:
    def __init__(self, db_type: str) -> None:
        db_class = db_map[db_type]
        self.db_connection = db_class()

    def retrieve_data(self) -> str:
        return self.db_connection.select_query()

    def optimize_db(self) -> str:
        if self.db_connection.check_db():
            return self.db_connection.add_index() + "\n" + \
                   self.db_connection.add_join()


if __name__ == "__main__":
    psql_orm = OrmProxy(db_type="postgres")
    print(psql_orm.retrieve_data())
    print("\n")
    print(psql_orm.optimize_db())
