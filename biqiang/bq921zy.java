package joe_prac;

public class bq921zy {
//	����Ĵ�����һ��
//	1.��ĳ�ԱȨ��ȫ��ʲô
//	public, private, default, protected
//	2.����Ȩ�޺�Ĭ��Ȩ�޵�������ʲô
//	����Ȩ�޿��Ա���ͬ���������ȡ��Ĭ��Ȩ�޲����Ա���ͬ���������ȡ��
//	3.���ڿ��Է���˽��Ȩ�޵ĳ�Ա��
//	����
//	4.������Ҫ�������е�˽�г�Աʱ������һ�����ô����
//		1������һ������Ȩ�ޣ����������Ȩ�޵���˽�г�Ա��2������һ�����࣬������Ĺ���Ȩ�޵������˽��Ȩ�ޣ�
//	5.һ���ʲô��Ա����Ϊ˽�е�
//	����
//	6.��дһ����Ϸ������,�����ļ���д,��Ϸ���������������,����,����,�Ա�,
//	д����Щ���Ե�getter��setter����,������Ա�Ҫ������ܸ�ֵ
	String name,clan,gender;
	int age;
	String getName(){
		return name;
	}
	String getClan(){
		return clan;
	}
	String getGender(){
		return gender;
	}
	int getAge() {
		return age;
	}
	void setName(String Name) {
		name=Name;
	}
	void setAge(int Age) {
		if(Age >= 0 & Age <=140 ) {
			age=Age;
		}
	}
	void setClan(String Clan) {
		clan=Clan;
	}
	void setGender(String Gender) {
		if(Gender=="��"|Gender=="Ů") {
			gender=Gender;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		bq921zy hero1= new bq921zy();
		hero1.setAge(18);
		hero1.setClan("�䵱");
		hero1.setGender("��");
		hero1.setName("������");
		System.out.println(hero1.getAge());
		System.out.println(hero1.getName());
		System.out.println(hero1.getClan());
		System.out.println(hero1.getGender());
		
		
		
		
		
		
		
		
		
		
		
		
	}

}
