package maker0921��������;

import maker.BB02����;


public class A02����Ȩ�� {

	

		//�й���Ȩ�޵ķ���
		public static void test() {
			System.out.println("test");
		}
		
		public static int a=20;
		public static void main(String[] args) {
			
			//1.���ñ��ļ������еĹ��г�Ա
			test();
			System.out.println(a);
			
			//2.����ͬһ�����������ļ�������Ĺ��г�Ա
			B02����  pp=new B02����();
			pp.test02();
			System.out.println(pp.mya);
			
			//3.���ñ�İ��е�����Ĺ��г�Ա
			
			BB02���� pu2=new BB02����();
			pu2.test03();
			System.out.println(pu2.myb);
			
			
			System.out.println(add(10,20));
			
			A���� aa=new A����();
			int arr[]= {1,23,45,65,76,34};
			int[] bb=aa.msort(arr);
			for(int i:bb) {
				System.out.print(i+" ");
			}
//	����:�ڱ��ļ���дһ������,������Ȩ���ǹ��е�,Ȼ����main��ʹ���������,��������Ĺ����Ǽӷ�����		
//	����:�ڱ���ļ�дһ����,������һ������,���������,Ȼ���ڱ��ļ�����ʹ��		
			
			
			
		}
		
		public static int add(int a,int b) {
			return a+b;
		}
		
		
		
	

}
