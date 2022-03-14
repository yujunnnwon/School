import java.util.Arrays;
import java.util.Scanner;

public class HW1 {
	public static void main(String[] args) {
		System.out.println("3개의 정수를 공백으로 분리하여 입력하시오.");
		Scanner scanner = new Scanner(System.in);
		
		// 3개의 정수를 입력받아 각각 a, b, c에 저장
		int a = scanner.nextInt();
		int b = scanner.nextInt();
		int c = scanner.nextInt();
		
		// 3개의 정수를 integer array로 저장
		int[] arr = {a, b, c};
		Arrays.sort(arr);				// Arrays의 메소드 sort를 사용하여 오름차순 정렬

		// 오름차순으로 정렬된 array의 인덱스를 차례대로 출력
		System.out.print(arr[0] + " ");
		System.out.print(arr[1] + " ");
		System.out.println(arr[2]);
		
		scanner.close();
	}
}