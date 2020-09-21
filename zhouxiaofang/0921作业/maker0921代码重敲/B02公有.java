package maker0921代码重敲;

public class B02公有 {
	
	public void test02() {
		System.out.println("B02公有的test02函数");
	}
	
	public int mya=100;
	
	//可以排序的方法
		public void mysort(int[] arr) {
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
