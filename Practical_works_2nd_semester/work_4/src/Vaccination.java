public class Vaccination extends MedicalCare {
    private String nameV;
    private String dataV;
    private String periodDo;
    public Vaccination(String name, String adress, String FIO, String polis, String date, String vrach, String dolznost, String diagnoz,
    		String nameV, String dataV, String periodDo){
    	super(name, adress, FIO, polis, date, vrach, dolznost, diagnoz);
        this.nameV = nameV;
        this.dataV = dataV;
        this.periodDo = periodDo;
    }
    
    public String getNameV() {
		return nameV;
	}

	public void setNameV(String nameV) {
		this.nameV = nameV;
	}

	public String getDataV() {
		return dataV;
	}

	public void setDataV(String dataV) {
		this.dataV = dataV;
	}

	public String getPeriodDo() {
		return periodDo;
	}

	public void setPeriodDo(String periodDo) {
		this.periodDo = periodDo;
	}

	public String toString() {
        return "\n" + super.toString() +
        		"\nНазвание вакцины: " + nameV + 
                "\nДата вакцинации: " + dataV + 
                "\nПериод действия: " + periodDo + '\n';
    }
}
