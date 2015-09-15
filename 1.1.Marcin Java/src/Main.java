
public class Main {

	/**
	 * Need files requests.csv,devices.csv,labels.csv in the same older
	 * @param args
	 */

	public static void main(String[] args) throws Exception {

		ReadRoqAttributes dataForClassification = new ReadRoqAttributes("requests.csv","devices.csv","labels.csv");
		
		//ReadStraz dataForClassification = new ReadStraz("straz.csv");
	}
}
