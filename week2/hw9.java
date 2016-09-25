import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class asd {

	public static void main(String[] args) {
		
		
		HashMap hm = new HashMap();
		
		String[] letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
		
		for (int i = 0 ; i < letters.length ; i++) {
			hm.put(letters[i],(int)(Math.random()* 10));
		}

		Set veriler = hm.entrySet();
		Set anahtarlar = hm.keySet();
		Collection degerler = hm.values();

		System.out.println("Datas : " + veriler);
		System.out.println("Keys : " + anahtarlar);
		System.out.println("Values : " + degerler);
		
		List<String> list = new ArrayList<String>(anahtarlar);
		//System.out.println(list);
		List<String> values = new ArrayList<String>(degerler);
		//System.out.println(values);
		
		Scanner x = new Scanner(System.in);
		System.out.println("Enter a character: ");
		char c = x.next().charAt(0);
		

		if (list.contains(String.valueOf(c))) {
			System.out.println("yes");
			System.out.println("character : " + c + " and the value is : " + hm.get(String.valueOf(c)));
		}
		else
			System.out.println("Enter a valid charachter!");
		
	}

}
