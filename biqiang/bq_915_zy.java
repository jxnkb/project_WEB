package joe_prac;

import java.util.Scanner;

public class bq_915_zy {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		1��While�����������������
//		������
//		2����ѭ��2����ѭ��4�Σ���ôһ��ѭ���˶��ٴ�
//		8��
//		3��Break����һ������2��ѭ����
//		������
//		4��������ʲô������������ʲô��
//		java���õ��������ͣ����Ե����У����ȹ̶����������䣬���б߽��飻
//		һ�������������ݵ�������
//		5���붨���һ�����Դ���8�����͵�����
//		int[] a1= new int[8];
//		6������⣺����Ԫ�ز���(����ָ��Ԫ�ص�һ���������г��ֵ�����)
		Scanner scanner=new Scanner(System.in);
//		int a1[]= {1,2,3,4,5,6,7,8,9};
//		System.out.println("����Ҫ�ҵ����֣�");
//		int b1=scanner.nextInt();
//		
//		for(int i=0;i<a1.length;i++) {
//			if(a1[i]==b1) {
//				System.out.println("����Ϊ"+i);
//			}
//		}
//		����:С��������ÿ�����2.5ԪǮ������������������ǣ�ÿ����һ���Ǵ�Ǯ�ĵ�5�����5�ı����Ļ���
//		�����Ứȥ6ԪǮ�����ʣ����������죬С���ſ��Դ浽100ԪǮ��
//		float u=2.5f;
//		int i;//day
//		for(i=1 ;u<100;i++) {
//			u+=2.5;
//			if(i%5==0) {
//				u-=6;
//			}
//		}
//		System.out.println(i);
//		
//		int day=0;
//		float money=0;
//		
//		while(money<100) {
//			money+=2.5;
//			day+=1;
//			if(day%5==0) {
//				money-=6;
//			}
//		}
//		System.out.println(day);
		
//		����:���1-100�ĵ���
		int a2=0;
		do {
			if(a2%2==1) {
				System.out.println(a2);
			}
			a2+=1;
		}while(a2<=100);
		
//		����:ʹ��whileǶ��ѭ����ӡ����ͼ��
//		*
//		* *
//		* * *
//		* * * *
//		* * * * *
		int i3=0;
		while(i3<5) {
			int u3=0;
			while(u3<=i3) {
				System.out.print('*');
				u3++;
			}
			i3++;
			System.out.println();
		}
		
//		����:����һ������,Ȼ���ӡ0���������,����ӡ0���������֮��
//		System.out.println("����һ��������");
//		int a4=scanner.nextInt(),b4=0;
//		for(int i4=0;i4<=a4;i4++) {
//			System.out.println(i4);
//			b4+=i4;
//		}
//		System.out.println(b4);
		
//		����:n�Ľ׳ˣ����ⲿ��������һ������n
//		System.out.println("����һ��������");
//		int a5=scanner.nextInt(),b5=1;
//		for(int i=1;i<=a5;i++) {
//			b5*=i;
//		}
//		System.out.println(b5);

//		����:�žų˷��ھ���
		
//		for(int i=1;i<=9;i++) {
//			for(int u=1;u<=i;u++) {
//				System.out.print(i+"*"+u+'='+u*i+"\t");
//			}
//			System.out.println();
//		}
		
//		��ӡ0-9������,��Ҫ��ӡ��5��
		for(int i=0;i<=9;i++) {
			if(i==5) {
				continue;
			}
			System.out.println(i);
			
		}
		
//		����:����һ������������,Ȼ��������,Ȼ�������ӡ
		int[] sz1=new int[10];
		for(int i=0;i<=9;i++) {
			sz1[i]=(int)(Math.random()*100);
		}
		for(int i:sz1) {
			System.out.print(i+" ");
		}
		System.out.println();
		for(int i=0,temp;i<sz1.length/2;i++) {
			temp=sz1[i];
			sz1[i]=sz1[sz1.length-1-i];
			sz1[sz1.length-1-i]=temp;
		}
		for(int i:sz1) {
			System.out.print(i+" ");
		}
		System.out.println();
		System.out.println("--------------------");
		
//		����:��һά�������ֵ
		int[] sz2=new int[10];
		for(int i=0;i<=9;i++) {
			sz2[i]=(int)(Math.random()*100);
		}
		for(int i:sz2) {
			System.out.print(i+" ");
			
		}
		System.out.println();
		int max=sz2[0],min=sz2[0];
		for(int i:sz2) {
			if(max<i) {
				max=i;
			}
			if(min>i) {
				min=i;
			}
			
			
		}
		System.out.println("���ֵ��"+max+"��Сֵ��"+min);
		
//		����:�ӿ���̨�����ַ���,Ȼ����ַ����е��ַ��洢���ַ�������,Ȼ���ӡ����
		System.out.println("�����ַ���:");
		String a7=scanner.next();
		char[] b7=new char[a7.length()];
		for(int i=0;i<a7.length();i++) {
			b7[i]=a7.charAt(i);
		}
		for(int i=0;i<b7.length;i++) {
			System.out.println(b7[i]);
		}
		
		
		
	}

}
