from typing import List




class University: 
    def __init__(self, name): 
        self.__name = name 


class Department(University): 
    def __init__(self, name , hod, course_offered): 
        super.__init__(name) 
        self.__hod = hod 
        self.__course_offered = course_offered







