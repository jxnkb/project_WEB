package maker0921代码重敲;

public class A00作业 {

	public static void main(String[] args) {
		// TODO 自动生成的方法存根

		int[] arr=createArr();
		
		printArr(arr);
		mysort(arr);
		System.out.println();
		printArr(arr);
		
	}
	
	//创建数组的函数
	public static int[] createArr() {
		int[] arr=new int[10];
		for(int i=0;i<arr.length;i++) {
			arr[i]=10+i;
		}
		return arr;
	}
	
	//打印数组的函数
	public static void printArr(int[] arr) {
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
	}
	
	//排序的函数
	public static void mysort(int[] arr) {
		for(int i=0;i<arr.length-1;i++) {
			for(int j=0;j<arr.length-1-i;j++) {
				if(arr[j]<arr[j+1]) {
					int tmp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=tmp;
				}
			}
		}
	}

}
