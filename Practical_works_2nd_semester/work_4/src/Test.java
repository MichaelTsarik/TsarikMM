import java.util.ArrayList;

public class Test {
	private ArrayList<MedicalCare> listOfMedicalCare;

	public Test(ArrayList<MedicalCare> listOfMedicalCare) {
		this.listOfMedicalCare = listOfMedicalCare;
	}

	public void addMedicalCare(MedicalCare MedicalCare) {
		listOfMedicalCare.add(MedicalCare);
	}

	public ArrayList<MedicalCare> printMedicalCare() {
		return listOfMedicalCare;
	}
	
	public static void main(String[] args) {
		ArrayList<MedicalCare> listOfMedicalCare = new ArrayList<>();
		Test test = new Test(listOfMedicalCare);
		
	    String name = "1 поликлиника";
	    String adress = "Советская 13";
	    String FIO = "Царик";
	    String polis = "987654";
	    String date = "20.06.2022";
	    String vrach = "Гагарина";
	    String dolznost = "Терапевт";
	    String diagnoz = "Здоров";
		String vid = "Стационарный"; 
		int Year = 2022; 
		String period = "2 Месяца"; 
		String result = "Выздоровление";
		String nameV = "ГамКовидВак";
	    String dataV = "20.06.2022";
	    String periodDo = "6 месяцев";
		String BirthСertificate = "777888999";
		String gender = "жен";
		String age = "2";
	    
		RoutineInspection routineInspection = new RoutineInspection(name, adress, FIO, polis, date, vrach, dolznost, diagnoz,
				vid, Year, period, result);
		test.addMedicalCare(routineInspection);
		
		Vaccination vaccination = new Vaccination(name, adress, FIO, polis, date, vrach, dolznost, diagnoz, nameV, dataV, periodDo);
		test.addMedicalCare(vaccination);
		
		Children deti = new Children(name, adress, FIO, polis, date, vrach, dolznost, diagnoz, BirthСertificate, gender, age);
		test.addMedicalCare(deti);
		
		System.out.print(test.printMedicalCare());
	}

}
