import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Set;

public class MyCode {

	public static void main(String[] args) {
		
		
		HashMap hm = new HashMap();
		
		/*hm.put("a" , (int)(Math.random()* 10));
		hm.put("b" , (int)(Math.random()* 10));
		hm.put("c" , (int)(Math.random()* 10));
		hm.put("d" , (int)(Math.random()* 10));
		hm.put("e" , (int)(Math.random()* 10));
		hm.put("f" , (int)(Math.random()* 10));
		hm.put("g" , (int)(Math.random()* 10));*/
		
		String[] letters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"};
		
		for (int i = 0 ; i < letters.length ; i++) {
			hm.put(letters[i],(int)(Math.random()* 10));
		}

		Set veriler = hm.entrySet();
		Set anahtarlar = hm.keySet();
		Collection degerler = hm.values();
		//Set veriler1 = hm.values();
		//int[] array1 = anahtarlar.toArray(new int[anahtarlar.size()]);
		//String[] array2 = veriler.toArray(new String[veriler.size()]);
		System.out.println("Verilerimiz : " + veriler);
		System.out.println("Anahtarlarz : " + anahtarlar);
		System.out.println("Degerler : " + degerler);
		
		List<String> list = new ArrayList<String>(anahtarlar);
		//System.out.println(list);
		List<String> values = new ArrayList<String>(degerler);
		//System.out.println(values);
		
		Scanner x = new Scanner(System.in);
		System.out.println("deger gir");
		char c = x.next().charAt(0);
		

		if (list.contains(String.valueOf(c))) {
			System.out.println("yes");
			System.out.println("character : " + c + " and the value is : " + hm.get(String.valueOf(c)));
		}
		else
			System.out.println("Enter a valid charachter!");
		
	}

}
