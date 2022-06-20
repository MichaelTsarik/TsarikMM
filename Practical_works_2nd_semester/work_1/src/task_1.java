/* 
    Номер зачетной книжки: 21-706.
    Автор: Царик Михаил Михайлович, ЗИТ-21
    Дата: 20.06.2022
    Реализовать программу, получающую на вход в качестве аргумента имя человека и выводящую "Hello, " + имя + "!",
    в противном случае, если параметр не передавался, "Hello World!".
*/

public class task_1 {
    public static void main(String[] name) {
        if (name.length > 0) { 
            System.out.print("Hello, " + name[0] + "!"); 
        } 
        else {
            System.out.print("Hello, World!"); 
        }
    }
}