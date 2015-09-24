import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.TimeZone;
import java.util.Vector;

public class ReadRoqAttributes {

	private String fileReq;
	private String fileDev;
	private String fileLabels;
	private String fileTimeZone;
	private String outputFile;
	String cvsSplitBy = ",";
	Random generator = new Random();
	
	private static final int deviceCount = 4000;
	
	public static final boolean  addrandom = false;
	Map<String,String> timeZones = new HashMap<String, String>();
	Map<String,String> cllusters = new HashMap<String, String>();
	
	public ReadRoqAttributes(String fileReq, String fileDev, String fileLabels, String fileTimeZone, String outputFile) {

		this.fileReq = fileReq;
		this.fileDev = fileDev;
		this.fileLabels = fileLabels;
		this.fileTimeZone = fileTimeZone;
		this.outputFile = outputFile;
		this.run();

	}

	public boolean isDouble(String input) {
		try {
			Double.parseDouble(input);
			return true;
		} catch (Exception e) {
			return false;
		}
	}

	public void getTimeZones() throws IOException{
		BufferedReader br = new BufferedReader(new FileReader(this.fileTimeZone));
		
		String line;
		while ((line = br.readLine()) != null) {

			String[] dane = line.split(cvsSplitBy);
			timeZones.put(dane[1],dane[0]);
			
			//System.out.println(dane[1] + " " + dane[0]);
		}
	}

	
	public void run() {
		
		generator.setSeed(System.currentTimeMillis());

		BufferedReader br = null;
		BufferedReader br2 = null;
		BufferedReader br3 = null;
		String line = "";

		try {

			Map<String, Integer> labels = new HashMap<String, Integer>(); // nonUnique DeviceID + random balanced ID's
			Map<String, String> nonunique = new HashMap<String, String>(); // nonunique UserID DeviceID
			
			Map<String, String> datta = new HashMap<String, String>(); // reading Devices description

			Map<String, Integer> requestsCount = new HashMap<String, Integer>(); 
			Map<String, String> timeZone = new HashMap<String, String>(); //timeZone

			Map<String, Integer> whoIswho = new HashMap<String, Integer>(); // Code ID into Integers

			//Readers
			br2 = new BufferedReader(new FileReader(fileDev));
			br3 = new BufferedReader(new FileReader(fileLabels));
			br = new BufferedReader(new FileReader(fileReq));
			int row = 0;

			//Attribute 1
			Map<String, Integer> Attr1czas = new HashMap<String, Integer>();
			int[][] Attr2country = new int[deviceCount][3];
			//Attribute 2
			int[][] countriesStats = new int[deviceCount][200];
			Map<String, Integer> countries = new HashMap<String, Integer>();
			int countriesCounter = 1;
			int kraj = 0;
			//Attribute 3
			Map<String, Integer> IPs = new HashMap<String, Integer>();
			int ipCount = 1;
			Vector<Vector<HashMap<Integer, Integer>>> myIPs = new Vector<Vector<HashMap<Integer, Integer>>>();
			for (int y = 0; y < deviceCount; y++) {
				myIPs.add(new Vector<HashMap<Integer, Integer>>());
				for (int yy = 0; yy < 24; yy++)
					myIPs.get(y).add(new HashMap<Integer, Integer>());
			}
			//Attribute 4
			Map<String, Integer> ISPs = new HashMap<String, Integer>();
			int ispCount = 1;
			Vector<Vector<HashMap<Integer, Integer>>> myISPs = new Vector<Vector<HashMap<Integer, Integer>>>();
			for (int y = 0; y < deviceCount; y++) {
				myISPs.add(new Vector<HashMap<Integer, Integer>>());
				for (int yy = 0; yy < 24; yy++)
					myISPs.get(y).add(new HashMap<Integer, Integer>());
			}
			//Attribute 5
			Map<String, Integer> Pages = new HashMap<String, Integer>();
			int pageCount = 1;
			Vector<Vector<HashMap<Integer, Integer>>> myPages = new Vector<Vector<HashMap<Integer, Integer>>>();
			for (int y = 0; y < deviceCount; y++) {
				myPages.add(new Vector<HashMap<Integer, Integer>>());
				for (int yy = 0; yy < 24; yy++)
					myPages.get(y).add(new HashMap<Integer, Integer>());
			}
			//Attribute 8
			int[][] connectionsStats = new int[deviceCount][6];
			Map<String, Integer> connections = new HashMap<String, Integer>();
			int connectionsCounter = 1;
			int[][] Attr8connections = new int[deviceCount][3];

			// / KONIEC DEFINICJI DANYCH

			getTimeZones(); // Read timeZones description
			
			Writer writer = new BufferedWriter(new OutputStreamWriter(
					new FileOutputStream(this.outputFile), "utf-8"));
			int[] licznik = new int[100];
			for (int i = 0; i < 100; i++)
				licznik[i] = 0;
			
			// Get non unique + random instances
			while ((line = br3.readLine()) != null) {

				String[] dane = line.split(cvsSplitBy);

				if(!nonunique.containsKey(dane[0]))
				{
					nonunique.put(dane[0], dane[1]);
					// ADD RANDOM BALANCED INSTANCES
					if (addrandom && generator.nextInt()%10 > 2) labels.put(dane[1],1);
				}
				else
				{
					labels.put(dane[1],1);
					labels.put(nonunique.get(dane[0]),1);
				}
				
			}
			
			// Get device description
			while ((line = br2.readLine()) != null) {

				String[] dane = line.split(cvsSplitBy);
				//line = line.replace(",,", ",X,");
				//line = line.replace(",,", ",X,");
				//line = line.replace(",,", ",X,");

				datta.put(dane[0], line);
				
			}

			// Read requests and compute attributes
			while ((line = br.readLine()) != null) {

				// use comma as separator
				String[] dane = line.split(cvsSplitBy);

				if (row >= 1 && labels.containsKey(dane[0])) {
					// System.out.println(dane[7]);

					
					
					Calendar cal;
					if (dane[5].length()>3) {cal = Calendar.getInstance(TimeZone.getTimeZone(timeZones.get(dane[5])));} 
					else { cal = Calendar.getInstance(); }
					cal.setTimeInMillis(new Long(dane[7]));

					timeZone.put(dane[0], dane[5]);

					// whoIswho
					if (!whoIswho.containsKey(dane[0])) {
						whoIswho.put(dane[0], kraj);
						kraj++;
					}
					int who = whoIswho.get(dane[0]);

					// Countries

					if (!countries.containsKey(dane[3])) {
						countries.put(dane[3], countriesCounter);
						countriesCounter++;
						countriesStats[who][countries.get(dane[3])]++;
					} else if (dane[3] != null) {
						countriesStats[who][countries.get(dane[3])]++;

					}

					// IPs
					if (!IPs.containsKey(dane[1])) {
						IPs.put(dane[1], ipCount);
						ipCount++;
					}

					if (dane[1] != null) {
						int ip = IPs.get(dane[1]);
						int hour = cal.get(Calendar.HOUR_OF_DAY);
						if (!myIPs.get(who).get(hour).containsKey(ip)) {
							myIPs.get(who).get(hour).put(ip, 1);
						} else {
							int ile = myIPs.get(who).get(hour).get(ip);
							myIPs.get(who).get(hour).put(ip, ile + 1);
						}
					}

					// ISPs
					if (!ISPs.containsKey(dane[2])) {
						ISPs.put(dane[2], ispCount);
						ispCount++;
					}

					if (dane[2] != null) {
						int isp = ISPs.get(dane[2]);
						int hour = cal.get(Calendar.HOUR_OF_DAY);
						if (!myISPs.get(who).get(hour).containsKey(isp)) {
							myISPs.get(who).get(hour).put(isp, 1);
						} else {
							int ile = myISPs.get(who).get(hour).get(isp);
							myISPs.get(who).get(hour).put(isp, ile + 1);
						}
					}

					// Pages
					int ppage = dane.length - 1;
					if (!Pages.containsKey(dane[ppage])) {
						Pages.put(dane[ppage], pageCount);
						pageCount++;
					}

					if (dane[ppage] != null) {
						int page = 1000000 * cal.get(Calendar.DAY_OF_YEAR)
								+ Pages.get(dane[ppage]);
						int hour = cal.get(Calendar.HOUR_OF_DAY);
						if (!myPages.get(who).get(hour).containsKey(page)) {
							myPages.get(who).get(hour).put(page, 1);
						} else {
							int ile = myPages.get(who).get(hour).get(page);
							myPages.get(who).get(hour).put(page, ile + 1);
						}
					}

					// Connections

					if (!connections.containsKey(dane[6])) {
						connections.put(dane[6], connectionsCounter);
						connectionsCounter++;
						connectionsStats[who][connections.get(dane[6])]++;
					} else if (dane[6] != null) {
						connectionsStats[who][connections.get(dane[6])]++;

					}

					// Attr1Czasowa

					if (!Attr1czas.containsKey(dane[0])) {
						int timeS = 1;
						int counter = cal.get(Calendar.HOUR_OF_DAY);
						while (counter > 0) {
							timeS = timeS << 1;
							counter--;
						}
						Attr1czas.put(dane[0], timeS);
					} else {
						int timeS = 1;
						int number = Attr1czas.get(dane[0]);
						int counter = cal.get(Calendar.HOUR_OF_DAY);
						while (counter > 0) {
							timeS = timeS << 1;
							counter--;
						}
						if ((number & timeS) == 0)
							number += timeS;
						// System.out.println(cal.get(Calendar.DAY_OF_YEAR));
						Attr1czas.put(dane[0], number);
					}

					// RequestyIle

					if (!requestsCount.containsKey(dane[0])) {
						requestsCount.put(dane[0], 0);
					} else {
						int ile = requestsCount.get(dane[0]);
						requestsCount.put(dane[0], ile + 1);
					}
				}

				row++;
			}
			System.out.print("KONIEC\n");

			// countryMAX,secondMAX,diff

			int cmax;
			int cmax2;
			int cdiff = 0;
			for (int i = 0; i < whoIswho.size(); i++) {
				cmax = 0;
				cmax2 = 0;
				cdiff = 0;
				for (int j = 0; j < countries.size(); j++) {
					if (countriesStats[i][j] > 0)
						cdiff++;
					// System.out.print(countriesStats[i][j] + " ");

					if (countriesStats[i][j] > cmax) {
						cmax2 = cmax;
						cmax = countriesStats[i][j];
						Attr2country[i][1] = Attr2country[i][0];
						Attr2country[i][0] = j;
					} else if (countriesStats[i][j] > cmax2) {
						cmax2 = countriesStats[i][j];
						Attr2country[i][1] = j;
					}
				}
				// System.out.println();
				Attr2country[i][2] = cdiff;
			}

			// connectionsMAX,secondMAX,connectionsdiff

			int connectionsmax;
			int connectionsmax2;
			int connectionsdiff = 0;
			for (int i = 0; i < whoIswho.size(); i++) {
				connectionsmax = 0;
				connectionsmax2 = 0;
				connectionsdiff = 0;
				for (int j = 0; j < connections.size(); j++) {
					if (connectionsStats[i][j] > 0)
						connectionsdiff++;
					// System.out.print(connectionsdiff);

					if (connectionsStats[i][j] > connectionsmax) {
						connectionsmax2 = connectionsmax;
						connectionsmax = connectionsStats[i][j];
						Attr8connections[i][1] = Attr8connections[i][0];
						Attr8connections[i][0] = j;
					} else if (connectionsStats[i][j] > connectionsmax2) {
						connectionsmax2 = connectionsStats[i][j];
						Attr8connections[i][1] = j;
					}
				}
				// System.out.println();
				Attr8connections[i][2] = connectionsdiff;
			}

			// WYPISYWANIE WYNIKU

			writer.write(datta.get("device_id") + ",");
			for (int y = 0; y < 24; y++)
				writer.write("Czas" + y + ",");
			writer.write("CountryDom,CountryDom2,CountryCount,");
			for (int y = 0; y < 24; y++)
				writer.write("IP" + y + ",");
			for (int y = 0; y < 24; y++)
				writer.write("ISP" + y + ",");
			writer.write("PageMax,PageMed,");
			writer.write("StartPageMax,StartPageMed,StartDays,");
			writer.write("ConnDom,ConnDom2,ConnDiff\n");

			List<String> lista = new LinkedList<String>(Attr1czas.keySet());
			Collections.sort(lista);
			//System.out.println(lista.size());
			for (String s : lista) {
				//System.out.println(s);
				int who = whoIswho.get(s);
				//System.out.println(who);
				int[] maxIP = new int[24];
				int[] whatIP = new int[24];
				for (int y = 0; y < 24; y++) {
					for (int now : myIPs.get(who).get(y).keySet()) {
						if (myIPs.get(who).get(y).get(now) > maxIP[y]) {
							maxIP[y] = myIPs.get(who).get(y).get(now);
							whatIP[y] = now;
						}
					}
				}
				int[] maxISP = new int[24];
				int[] whatISP = new int[24];
				for (int y = 0; y < 24; y++) {
					for (int now : myISPs.get(who).get(y).keySet()) {
						if (myISPs.get(who).get(y).get(now) > maxISP[y]) {
							maxISP[y] = myISPs.get(who).get(y).get(now);
							whatISP[y] = now;
						}
					}
				}

				int maxPages = 0;
				List<Integer> Pp = new ArrayList<Integer>();
				List<Integer> startingPage = new ArrayList<Integer>();
				int start = 0;
				for (int y = 0; y < 24; y++) {
					int hour = y;
					for (int now : myPages.get(who).get(hour).keySet()) {
						Pp.add(myPages.get(who).get(hour).get(now));
						// System.out.println(start);
						if (start == 0 || start != now / 1000000) {
							start = now / 1000000;
							startingPage.add(myPages.get(who).get(y).get(now));
						}
						if (myPages.get(who).get(y).get(now) > maxPages) {
							maxPages = myPages.get(who).get(y).get(now);

						}
					}
				}
				Collections.sort(Pp);
				Collections.sort(startingPage);

				writer.write(datta.get(s) + ", ");

				String sBin = String.format("%24s",
						Integer.toBinaryString(Attr1czas.get(s))).replace(' ',
						'0');
				for (int i = 0; i < sBin.length(); i++) {
					writer.write(sBin.charAt(i) + ",");
				}

				writer.write(Attr2country[who][0] + "," + Attr2country[who][1]
						+ "," + Attr2country[who][2] + ",");
				for (int y = 23; y >= 0; y--)
					writer.write(whatIP[y] + ",");
				for (int y = 23; y >= 0; y--)
					writer.write(whatISP[y] + ",");
				writer.write(maxPages + "," + Pp.get(Pp.size() / 2));
				writer.write("," + startingPage.get(startingPage.size() - 1)
						+ "," + startingPage.get(startingPage.size() / 2)
						+ "," + startingPage.size());
				writer.write("," + Attr8connections[who][0] + ","
						+ Attr8connections[who][1] + ","
						+ Attr8connections[who][2]);
				/*
				if(cllusters.containsKey(s)) { 
				writer.write(cllusters.get(s)); }
				else writer.write(String.valueOf(generator.nextInt(30)+1));				
				*/
				writer.write("\n");
				writer.flush();
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			//e.printStackTrace();
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}

		System.out.println("Done");
	}

}
