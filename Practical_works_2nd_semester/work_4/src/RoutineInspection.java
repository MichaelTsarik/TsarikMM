public class RoutineInspection extends MedicalCare{
	private String vid; 
	private int Year; 
	private String period; 
	private String result;
	
	public RoutineInspection(String name, String adress, String FIO, String polis, String date, String vrach, String dolznost, String diagnoz, 
			String vid, int Year, String period, String result) {
		super(name, adress, FIO, polis, date, vrach, dolznost, diagnoz);
		this.vid = vid;
		this.Year = Year;
		this.period = period;
		this.result = result;
		
	}

	public String getVid() {
		return vid;
	}

	public void setVid(String vid) {
		this.vid = vid;
	}

	public int getYear() {
		return Year;
	}

	public void setYear(int year) {
		Year = year;
	}

	public String getPeriod() {
		return period;
	}

	public void setPeriod(String period) {
		this.period = period;
	}

	public String getResult() {
		return result;
	}

	public void setResult(String result) {
		this.result = result;
	}
	public String toString() {
        return "\n" + super.toString() +
        		"\nВид осмотра: " + vid +
        		"\nГод проведения: " + Year +
        		"\nПериод действия: " + period +
        		"\nРезультат осмотра: " + result + "\n";
    }
	
}
