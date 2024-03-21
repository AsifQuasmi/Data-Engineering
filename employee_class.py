class employee:
    def func(self,employee_id,name,salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        print(f"Details of epmloyee is : {self.employee_id} as employeed id {self.name} as name {self.salary} as salary")
    
obj = employee()
obj.func(1,"Asif",2000)