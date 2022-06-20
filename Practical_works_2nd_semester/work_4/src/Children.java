public class Children extends MedicalCare {
	  private String BirthСertificate;
	  private String gender;
	  private String age;
	  public Children(String name, String adress, String FIO, String polis, String date, String vrach, String dolznost, String diagnoz,
					  String BirthСertificate, String gender, String age){
	    	super(name, adress, FIO, polis, date, vrach, dolznost, diagnoz);
	        this.BirthСertificate = BirthСertificate;
	        this.gender = gender;
	        this.age = age;
	    }
	   
	public String getBirthСertificate() {
	return BirthСertificate;
	}

	public void setBirthСertificate(String birthСertificate) {
		BirthСertificate = birthСertificate;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public String getAge() {
		return age;
	}

	public void setAge(String age) {
		this.age = age;
	}

		public String toString() {
	        return "\n" + super.toString() +
	        		"\nСвидетельство орождении: " + BirthСertificate + 
	                "\nПол: " + gender + 
	                "\nВозраст ребёнка: " + age + '\n';
	    }
}
