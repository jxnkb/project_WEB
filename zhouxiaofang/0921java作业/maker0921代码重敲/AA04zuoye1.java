package maker0921��������;

public class AA04zuoye1 {

	

//	6.	��дһ����Ϸ������,�����ļ���д,��Ϸ���������������,����,����,�Ա�,
//	д����Щ���Ե�getter��setter����,������Ա�Ҫ������ܸ�ֵ

		
		private String name;
		private int age;
		private String menpai;
		private String sex;
		
		//��������
		void setName(String name1) {
			name=name1;
		}
		
		//��ȡ����
		String getName() {
			return name;
		}
		
		
		//��������
		void setAge(int age1) {
			if(age1>0 && age1<140) {
				age=age1;
			}else {
				System.out.println("��������䲻�Ϸ�");
			}
			
		}			
		//��ȡ����
		int getAge() {
			return age;
		}
		
		//��������
		void setMenpai(String menpai1) {
			menpai=menpai1;
		}
		
		//��ȡ����
		String getMenpai() {
			return menpai;
		}
		
		//�����Ա�
		void setSex(String sex1) {
			if(sex1=="��" || sex1=="Ů" ) {
				sex=sex1;
			}else {
				System.out.println("������Ա𲻺Ϸ�");
			}
					
		}			
		//��ȡ�Ա�
		String getSex() {
			return sex;
		}
		
	
		
}	


