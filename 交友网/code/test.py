from .mysql import Mysql

my01 = Mysql()

# print(my01.query("select *from person where id=%s", list_paramers=[20], size=1))
# str = "id"
# print(my01.in_up_de("update person set id=10 where id=%s", [2]))
# print(my01.batch_in_up_de([["update person set id=%s where id=%s",
#                          [(10, 1), (20, 2)]],["delete from person where id=%s",
#                                               [1, 2]]]))
#
# my01.close()
