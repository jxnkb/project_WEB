package maker0921��������;

public class A00��ҵ {

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������

		int[] arr=createArr();
		
		printArr(arr);
		mysort(arr);
		System.out.println();
		printArr(arr);
		
	}
	
	//��������ĺ���
	public static int[] createArr() {
		int[] arr=new int[10];
		for(int i=0;i<arr.length;i++) {
			arr[i]=10+i;
		}
		return arr;
	}
	
	//��ӡ����ĺ���
	public static void printArr(int[] arr) {
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
	}
	
	//����ĺ���
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
