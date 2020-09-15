package maker2代码重敲;

public class A07数组 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		
		//1.定义数组
		int a=5;
		int[] arr=new int[5]; //只是开辟了空间
		int[] arr1=new int[a]; //只是开辟了空间
		arr[0]=10;
		arr[1]=20;
		arr[2]=30;
		arr[3]=40;
		arr[4]=50;
	//	arr[5]=60; 报错
		
		for(int i=0;i<5;i++) {
			arr[i]=(i+1)*10;
			System.out.println(arr[i]);
		}
		
		//2.定义数组,分步
		int[] arr2=null;
		int a1=3;
		arr2=new int[a1];
		arr2[0]=100;
		arr2[1]=200;
		arr2[2]=300;
		
		
		//3.可以这样打印
		for(int i:arr2) {
			System.out.println(i);
			
		}
		
		//4.定义数组并初始化
		int arr3[]= {1,2,3,4,5,6,7};
		for(int i=0;i<arr3.length;i++) {
			System.out.println(arr3[i]+" ");
		}
		
		
//		案例:定义一个整型数数组,然后赋予数据,然后逆序打印
		//1.用随机数给数组赋值
		//2.遍历数组
		//3.逆序
		//	1.{1,2,3,4}
			//arr[0]=1;
		//	arr[3]=4;
		//4.遍历数组
		
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
		
		
//		案例:求一维数组的最值
		/*
		 * 1.用随机数给数组赋值
		 * 2.遍历数组
		 * 3.求数组的最大值
		 * 	//1.定义一个变量,用来存储最大值
		 * 	//2.假设数组第一个元素是最大值
		 *  //3.遍历数组时进行判断,如果有元素比变量存储的数值更大,那么就把这个数赋值给变量
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
		max=myarr2[0]; //假设数组的第一数是最大值
		for(int i=1;i<myarr2.length;i++) {
			if(max<myarr2[i]) { //如果进入if,表示数组里有比max更大的数
				max=myarr2[i];
			}
		}
		
		System.out.println("max="+max);
		
		
		

	}

}
