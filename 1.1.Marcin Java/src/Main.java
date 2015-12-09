public class Main {

	/**
	 * Need files requests.csv,devices.csv,labels.csv in the same older
	 * @param args
	 */

	public static void main(String[] args) throws Exception {

		System.out.println(args[0] + "requests.csv");

		ReadRoqAttributes dataForClassification = new ReadRoqAttributes(args[0] + "requests.csv", args[0] + "devices.csv", args[0] + "labels.csv");
		
		//ReadStraz dataForClassification = new ReadStraz("straz.csv");
	}
}
