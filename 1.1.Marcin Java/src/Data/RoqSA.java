package Data;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.util.ArrayList;

public class RoqSA {
	
	String file;
	String line = "";
	String cvsSplitBy = ",";
	
	RoqSA(String file){
		this.file = file;
	}
	
	public void Predict(){
		try {
			BufferedReader br = new BufferedReader(new FileReader(file));
			
			ArrayList<String> types = new ArrayList<String>();
			
			Writer writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream("result.csv"), "utf-8"));
			
			int row=0;
			
			while ((line = br.readLine()) != null) {
				String[] dane = line.split(cvsSplitBy);
			
				if(row==0) {
					for(int i=0;i<dane.length;i++) {
						types.add(dane[i]);	
					}
					
				} else { // ROW >1
					
				}
				
				row++;
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
