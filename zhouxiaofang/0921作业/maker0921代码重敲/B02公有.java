package maker0921��������;

public class B02���� {
	
	public void test02() {
		System.out.println("B02���е�test02����");
	}
	
	public int mya=100;
	
	//��������ķ���
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
