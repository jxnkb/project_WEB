package Testmaker��������;

public class A05Test����� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		//1.���������
		int a=10;
		int b=20;
		int c1=a+b;
		int c2=a-b;
		int c3=a*b;
		int c4=a/b;
		int c5=a%b;
		c5++;
		--c5;
		System.out.println(c1); //30
		System.out.println(c2); //-10
		System.out.println(c3); //200
		System.out.println(c4); //0
		System.out.println(c5); //10
		
		//2.��ֵ�����
		int x=10;
		x+=1; //11
		x-=2; //9
		x*=10; //90
		x/=2;  //45
		x%=2;  //1
		System.out.println(x);  //1
		
		
		//3.�Ƚ������
		int y=20;
		int z=10; 
		System.out.println(y==z); //false
		System.out.println(y!=z); //true
		System.out.println(y>z);  //true
		System.out.println(y<z);  //false
		System.out.println(y>=z); //true
		System.out.println(y<=z); //false
		//instanceof�����ж�һ��ʵ���Ƿ����ĸ��������ɵ�
		System.out.println("hello" instanceof String);
		System.out.println("--------");
		
		
		
		//4.�߼������
		boolean k=true;
		boolean kk=false;
		System.out.println(k&kk); //false
		System.out.println(k&&kk);  //false
		System.out.println(k|kk);  //true
		System.out.println(k||kk); //true
		System.out.println(k^kk);  //true
		System.out.println(!kk);   //true
		
		
		//5.λ����
		int a1=10;
		int b1=8;
		/*
		 * 0000 1010
		 * 0000 1000
		 * 0000 1000-->8
		 * 
		 */
		int d1=a1&b1;
		System.out.println(d1);
		
		
	}

}
