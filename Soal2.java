import java.util.List;
import java.util.ArrayList;
public class Soal2 {
    public static void main(String[] args) {
        String input =
                "Charlie,Zoe,08123123123;Andre,Xavier,08111222333;Charlie,Xyz,08123123123;Jean,Summers,08001001001";
        String[] stringContacts = input.split(";");
        Phonebook phonebook = new Phonebook();

        System.out.println("Input");
        System.out.println(input + "\n");
        System.out.println("Output");

        System.out.println("=== OUTPUT START ===");
        System.out.println("Log ");

        for (String stringContact : stringContacts) {
            String splitString[] = stringContact.split(",");
            Contact contact = new Contact(splitString[0], splitString[1], splitString[2]);
            phonebook.append(contact);
        }

        System.out.println("");
        System.out.println("Phone Book: ");
        phonebook.getList();
        System.out.println("=== OUTPUT END ===");


    }


}

class Contact
{
    private  String first_name;
    private String last_name;
    private  String phone;

    public  Contact(String first_name, String last_name, String phone){
        this. first_name = first_name;
        this.last_name  = last_name;
        this.phone = phone;
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getLast_name() {
        return last_name;
    }

    public String getPhone() {
        return phone;
    }

    public String getFullname() {
        return  this.first_name + " " + this.last_name;
    }

    public String get_phonebook() {
        return this.getFullname() + " - " + this.getPhone();
    }



}

class Phonebook
{
    public  List<Contact> contacts;

    public Phonebook() {
        this.contacts = new ArrayList<Contact>();
    }

    public void append( Contact contacts) {
        boolean numberexist = this.is_exists_phone(contacts.getPhone());
        if (numberexist != true){
            this.contacts.add(contacts);
            System.out.println(
                    contacts.getFullname() + " - " + contacts.getPhone() + " : "+"insert success"
            );

        }else {
            System.out.println(
                    contacts.getFullname() + " - " + contacts.getPhone() + " : "+"Duplicate phone number");
        }

    }

    public boolean is_exists_phone(String phone) {
        for (Contact contact : this.contacts){
            if(contact.getPhone().equals(phone)){
                return true;
            }
        }
        return false;
    }


    public void getList() {
        int a = 1 ;
        for (Contact contact : this.contacts){
            System.out.println(" " + (a++) + ". "+ contact.get_phonebook() );
        }
    }
}

