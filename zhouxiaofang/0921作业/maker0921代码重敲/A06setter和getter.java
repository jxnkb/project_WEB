package maker0921��������;

public class A06setter��getter {
	
	
	public static class Maker{
		private int age=10;
		
		int getAge() {
			return age;
		}
		
		void setAge(int age1) {
			if(age1>0 && age1<140) {
				age=age1;
			}else {
				System.out.println("��������䲻�Ϸ�");
			}
			
		}
	}

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������

		Maker m=new Maker();
		int a=m.getAge();
		System.out.println(a); //10
		m.setAge(18);
		a=m.getAge();
		System.out.println(a); //18
		
		
		Users n=new Users();
		n.setName("maker");
		System.out.println(n.getName());
		
		n.setIpthon("12345678901");
		System.out.println(n.getIpthon());
		
		n.setPasswd("1234567","1234567891");
		System.out.println(n.getPasswd());
		
//����:���һ���û���,������˽�г�Ա����������,�绰����.���������˽�����Ե�setter��getter����
//�����޸�������Ҫ��֤�绰����		
	}
	
	public static class Users{
		private String name="mmm";
		private String passwd="123456";
		private String ipthon="15770835722";
		
		//��������
		void setName(String name1) {
			name=name1;
		}
		//��ȡ����
		String getName() {
			return name;
		}
		
		//���õ绰����
		void setIpthon(String ipthon1) {
			ipthon=ipthon1;
		}
		//��ȡ�绰����
		String getIpthon() {
			return ipthon;
		}
				
		//��������
		void setPasswd(String passwd1,String ipthon2) {
			if(ipthon2==ipthon) {
				passwd=passwd1;
			}else {
				System.out.println("����ĵ绰���벻��ȷ");
			}
			
		}
		//��ȡ����
		String getPasswd() {
			return passwd;
		}
		
	}
	
	
	
	
	

}
