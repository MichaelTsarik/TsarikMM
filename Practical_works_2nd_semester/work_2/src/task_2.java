/*
    Номер зачетной книжки: 21-706.
    Автор: Царик Михаил Михайлович, ЗИТ-21
    Дата: 20.06.2022
    Вариант-13. Задача 2.
*/

import java.util.Arrays;
import java.util.Scanner;

public class task_2 {

    public static void main(String[] args) {
        System.out.print("Введите размер массива: ");
        Scanner scan = new Scanner(System.in);
        int size = scan.nextInt();
        double[] b = new double[size];

        // Заполнение массива случайными числами
        for (int i = 0; i < b.length; i++) {
            b[i] = ((int)(Math.random() * 31) - 15);
        }

        // Вывод массива
        System.out.println("Массив В ");
        System.out.println(Arrays.toString(b));

        // Перенос положительных чисел в другой массив
        int counter = 0;
        double[] c = new double[b.length];
        for (int i = 0; i < c.length; i++) {
            if (b[i] > 0) {
                c[counter] = b[i] / 5;
                counter++;
            }
        }
        // Сжатие массива
        c = Arrays.copyOf(c, counter);

        // Сортировка
        for (int left = 0; left < c.length; left++) {
            int minInd = left;
            for (int i = left; i < c.length; i++) {
                if (c[i] < c[minInd]) {
                    minInd = i;
                }
            }
            swap(c, left, minInd);
        }

        System.out.println("Массив С: ");
        System.out.println(Arrays.toString(c));
    }

    private static void swap(double[] array, int ind1, int ind2) {
        double tmp = array[ind1];
        array[ind1] = array[ind2];
        array[ind2] = tmp;
    }
}