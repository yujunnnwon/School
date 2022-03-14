import java.util.Scanner;

public class HW3 {	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.println("어떠한 화폐 단위를 환전하겠습니까? (원: 1, 유로: 2, 엔: 3)");
		int input = scanner.nextInt();		// 환전을 할 화폐 단위를 입력받음
		
		System.out.println("어떠한 화폐 단위로 환전하겠습니까? (원: 1, 유로: 2, 엔: 3)");
		int output = scanner.nextInt();		// 환전 기준이 되는 화폐 단위를 입력받음
		
		if (input == 1) {
			if (output == 1) {				// 원 -> 원
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "원은 " + money + "원입니다.");
			}
			else if (output == 2) {			// 원 -> 유로
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "원은 " + (money * 0.00074) + "유로입니다.");
			}
			else if (output == 3) {			// 원 -> 엔
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "원은 " + (money * 0.095) + "엔입니다.");
			}
		}
		else if (input == 2) {
			if (output == 1) {				// 유로 -> 원
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "유로는 " + (money * 1354.18) + "원입니다.");
			}
			else if (output == 2) {			// 유로 -> 유로
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "유로는 " + money + "유로입니다.");
			}
			else if (output == 3) {			// 유로 -> 엔
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "유로는 " + (money * 128.58) + "엔입니다.");
			}
		}
		else if (input == 3) {
			if (output == 1) {				// 엔 -> 원
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "엔은 " + (money * 10.53) + "원입니다.");
			}
			else if (output == 2) {			// 엔 -> 유로
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "엔은 " + (money * 0.0078) + "유로입니다.");
			}
			else if (output == 3) {			// 엔 -> 엔
				System.out.println("얼마를 환전하겠습니까?");
				int money = scanner.nextInt();
				System.out.println(money + "엔은 " + money + "엔입니다.");
			}
		}
		
		scanner.close();
	}
}
