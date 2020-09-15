package maker2代码重敲;

public class A01while {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
//		int a=10;
	//	while(a) { //报错,不是布尔型
			
//		}
		
	//    boolean b=true;
	//    while(b) {
	    	
	//    }
	
	int a1=1;
	while (a1<=5) {
//		System.out.println(a1);	
		System.out.print(a1+" ");
		a1++;
	}
	
//	案例:小芳的妈妈每天给她2.5元钱，她都会存起来，但是，每当这一天是存钱的第5天或者5的倍数的话，
//	她都会花去6元钱，请问，经过多少天，小芳才可以存到100元钱。
	/*
	 * 1.如果存储钱的数量打印100,那么就跳出循环
	 * 2.day%5==0  钱-6
	 */
	//钱
	double m=0;
	int day=0;
	while(m<=100) {
		m+=2.5;
		day+=1;
		if(day%5==0) {
			m=m-6;
		}
	}
	
	System.out.println(day);
	
	
	
		

	}

}
