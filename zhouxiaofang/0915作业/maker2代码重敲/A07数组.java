package maker2��������;

public class A07���� {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		
		//1.��������
		int a=5;
		int[] arr=new int[5]; //ֻ�ǿ����˿ռ�
		int[] arr1=new int[a]; //ֻ�ǿ����˿ռ�
		arr[0]=10;
		arr[1]=20;
		arr[2]=30;
		arr[3]=40;
		arr[4]=50;
	//	arr[5]=60; ����
		
		for(int i=0;i<5;i++) {
			arr[i]=(i+1)*10;
			System.out.println(arr[i]);
		}
		
		//2.��������,�ֲ�
		int[] arr2=null;
		int a1=3;
		arr2=new int[a1];
		arr2[0]=100;
		arr2[1]=200;
		arr2[2]=300;
		
		
		//3.����������ӡ
		for(int i:arr2) {
			System.out.println(i);
			
		}
		
		//4.�������鲢��ʼ��
		int arr3[]= {1,2,3,4,5,6,7};
		for(int i=0;i<arr3.length;i++) {
			System.out.println(arr3[i]+" ");
		}
		
		
//		����:����һ������������,Ȼ��������,Ȼ�������ӡ
		//1.������������鸳ֵ
		//2.��������
		//3.����
		//	1.{1,2,3,4}
			//arr[0]=1;
		//	arr[3]=4;
		//4.��������
		
		int[] myarr=new int[5];
		for(int i=0;i<5;i++) {
			myarr[i]=(int)(Math.random()*100);
		}
		for(int i:myarr) {
			System.out.print(i+" ");
		}
		//{55 93 90 39 40 }
		// 0   1  2  3  4
//		int a=55;
//		int b=40;
//		int tmp=a;
//		a=b;
//		b=tmp;
		
		for(int i=0;i<myarr.length/2;i++) {
			int tmp=myarr[i];
			myarr[i]=myarr[myarr.length-1-i];
			myarr[myarr.length-1-i]=tmp;
		}
		System.out.println();
		for(int i:myarr) {
			System.out.print(i+" ");
		}
		System.out.println("-----------");
		
		
//		����:��һά�������ֵ
		/*
		 * 1.������������鸳ֵ
		 * 2.��������
		 * 3.����������ֵ
		 * 	//1.����һ������,�����洢���ֵ
		 * 	//2.���������һ��Ԫ�������ֵ
		 *  //3.��������ʱ�����ж�,�����Ԫ�رȱ����洢����ֵ����,��ô�Ͱ��������ֵ������
		 */		
		int[] myarr2=new int[5];
		for(int i=0;i<5;i++) {
			myarr2[i]=(int)(Math.random()*100);
		}
		for(int i:myarr2) {
			System.out.print(i+" ");
		}
		System.out.println();
		int max=0;
		max=myarr2[0]; //��������ĵ�һ�������ֵ
		for(int i=1;i<myarr2.length;i++) {
			if(max<myarr2[i]) { //�������if,��ʾ�������б�max�������
				max=myarr2[i];
			}
		}
		
		System.out.println("max="+max);
		
		
		

	}

}
