# публичный, без особого синтаксиса: attribute_name
# защищённый, с однич подчеркиванием: _attribute_name
# приватный, с двойным подчеркиванием: __attribute_name

class Phone:    
    username = "Kate"  # public variable
    __how_many_times_turned_on = 0  # private variable
    
    def call(self):  # public method
        print( "Ring-ring!" )    
    
    def __turn_on(self):  # private method
        self.__how_many_times_turned_on += 1         
        print( "Times was turned on: ", self.__how_many_times_turned_on )
        

my_phone = Phone()
my_phone.call()
print("The username is ", my_phone.username ) 
# my_phone.turn_on()
# AttributeError: 'Phone' object has no attribute 'turn_on'
# my_phone.__turn_on()
# AttributeError: 'Phone' object has no attribute '__turn_on'
# print("Turned on: ", my_phone.__how_many_times_turned_on)
# AttributeError: 'Phone' object has no attribute '__how_many_times_turned_on'.
# print("Turned on: ", my_phone.how_many_times_turned_on)
# AttributeError: 'Phone' object has no attribute 'how_many_times_turned_on'.

my_phone._Phone__turn_on()
my_phone._Phone__how_many_times_turned_on = 10
my_phone._Phone__turn_on()