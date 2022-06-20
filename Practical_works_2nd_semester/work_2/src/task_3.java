/*
    Номер зачетной книжки: 21-706.
    Автор: Царик Михаил Михайлович, ЗИТ-21
    Дата: 20.06.2022
    Вариант-13. Задача 3.
*/

public class task_3 {
	  public static void main(String[] args) {
		  System.out.println("Матрица: ");
		  int n = 5;
		  int[][] mass = new int[n][n];
	      for (int i = 0; i < n; i++){
			  for (int j = 0; j < n; j++){
	            	mass[i][j] = ((int) (Math.random() * 31)-15);
	            	System.out.print(mass[i][j] + "\t");
			  }
			  System.out.println();
		  }
	  }
}
