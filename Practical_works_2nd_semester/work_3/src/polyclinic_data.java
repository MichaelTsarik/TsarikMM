/*
    Номер зачетной книжки: 21-706.
    Автор: Царик Михаил Михайлович, ЗИТ-21
    Дата: 20.06.2022
    Вариант-13. Polyclinic
*/

public class polyclinic_data {
    private String name;
    private String adress;
    private String FIO;
    private String polis;
    private String date;
    private String vrach;
    private String dolznost;
    private String diagnoz;
    public polyclinic_data(String name, String adress, String FIO, String polis, String date, String vrach, String dolznost, String diagnoz) {
        this.name = name;
        this.adress = adress;
        this.FIO = FIO;
        this.polis = polis;
        this.date = date;
        this.vrach = vrach;
        this.dolznost = dolznost;
        this.diagnoz = diagnoz;
    }
    public String getname() {
        return name;
    }
    public void setname(String name) {
        this.name = name;
    }
    public String getadress() {
        return adress;
    }
    public void setadress(String adress) {
        this.adress = adress;
    }
    public String getFIO() {
        return FIO;
    }
    public void setFIO(String FIO) {
        this.FIO = FIO;
    }
    public String getpolis() {
        return polis;
    }
    public void setpolis(String polis) {
        this.polis = polis;
    }
    public String getdate() {
        return date;
    }
    public void setdate(String date) {
        this.date = date;
    }
    public String getvrach() {
        return vrach;
    }
    public void setvrach(String vrach) {
        this.vrach = vrach;
    }
    public String getdolznost() {
        return dolznost;
    }
    public void setdolznost(String dolznost) {
        this.dolznost = dolznost;
    }
    public String getdiagnoz() {
        return diagnoz;
    }
    public void setdiagnoz(String diagnoz) {
        this.diagnoz = diagnoz;
    }
    public String toString()
    {
        return " Название поликлиники: " + name + ";\n Адрес: " + adress + ";\n Фамилия пациента: "+FIO+";\n Номер полиса: "+polis+";\n Дата осмотра: "+date+";\n Фамилия врача "+vrach+";\n Должность врача: "+dolznost+";\n Диагноз: "+diagnoz+".";
    }
}
