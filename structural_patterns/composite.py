from abc import ABC, abstractmethod


class IDepartment(ABC):
    @abstractmethod
    def __init__(self, employees: int) -> None:
        """"""

    @abstractmethod
    def print_dept_info(self) -> str:
        """"""


class Development(IDepartment):
    def __init__(self, emp_count: int) -> None:
        self.emp_count = emp_count

    def print_dept_info(self) -> str:
        return f"Number of employees in Dept Development:{self.emp_count}"


class Support(IDepartment):
    def __init__(self, emp_count: int) -> None:
        self.emp_count = emp_count

    def print_dept_info(self) -> str:
        return f"Number of employees in Dept Support:{self.emp_count}"


class GozenSystemsDept(IDepartment):
    def __init__(self, emp_count: int) -> None:
        self.base_emp_count = emp_count
        self.emp_count = emp_count
        self.sub_depts = list()

    def add_dept(self, dept: IDepartment) -> None:
        self.sub_depts.append(dept)
        self.emp_count += dept.emp_count

    def print_dept_info(self) -> str:
        dept_info = f"Base emp count in Dept Gozen Sys:{self.base_emp_count}\n"
        for dept in self.sub_depts:
            dept_info += f"{dept.print_dept_info()}\n"
        dept_info += f"Total employee count:{self.emp_count}\n"
        return dept_info


if __name__ == "__main__":
    dev_dept = Development(emp_count=30)
    print(f"{dev_dept.print_dept_info()}\n")

    support_dept = Support(emp_count=50)
    print(f"{support_dept.print_dept_info()}\n")

    gozen_sys_dept = GozenSystemsDept(emp_count=10)
    gozen_sys_dept.add_dept(dev_dept)
    gozen_sys_dept.add_dept(support_dept)
    print(f"{gozen_sys_dept.print_dept_info()}\n")
