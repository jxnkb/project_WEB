package zy922;

public class a2 {
	//����:���һ���û���,������˽�г�Ա����������,�绰����.���������˽�����Ե�setter��getter����
			//�����޸�������Ҫ��֤�绰����
	static class usr{
		private String name,phone,password;
		String getname(){
			return name;
		}
		String getphone() {
			return phone;
		}
		String getpassword() {
			return password;
		}
		public void setname(String name) {
			this.name=name;
		}
		public void setpassword(String password,String phone) {
			if(this.phone.equals(phone) ) {
				this.password=password;
			}else {
				System.out.println("�������");
			}
		}
		public void setphone(String phone) {
			this.phone=phone;
		}
	}
	
//	����:�ڱ���ļ�����һ����,����������name,age,score,����age��ֵʱҪ�жϺϷ���
//	����ͨ�����캯����ֵ,���Ե��ô�ӡ��Щ���Եķ���
	static class guy{
		String name;
		int age,score;
		guy(String name,int age,int score){
			this.name=name;
			if(age>0 &age<140) {
				this.age=age;
			}else {
				System.out.println("���벻�Ϸ�");
			}
			this.score=score;
		}
		void getinfo(){
			System.out.println("������"+name+" ����:"+age+" ������"+score);
		}
	}
	
	
//	���һ��������,�����з����,��λ��,������,�����������Ե�setter��getter����,Ҫ���β�����������һ��
	static class room{
		String num,name;
		int seats;
		void setnum(String num){
			this.num=num;
		}
		void setname(String name) {
			this.name=name;
		}
		void setseats(int seats) {
			this.seats=seats;
		}
		String getname() {
			return name;
		}
		String getnum() {
			return num;
		}
		int getseats() {
			return seats;
		}
	}
	
	
//	����:��װһ������,����������,����,Ʒ��,�ṩ����ӿ�,ͨ���ӿڲ��ܷ������Ժ��޸�����,
//	�޸���������ʱ��Ҫ��֤�Ϸ���.�й��캯���ȸ���Щ���Ը�ֵ
	static class dog{
		private String name,breed;
		private int age;
		dog(String name,String breed,int age){
			this.name=name;
			this.breed=breed;
			this.age=age;
		}
		public int getAge() {
			return age;
		}
		public String getBreed() {
			return breed;
		}
		public String getName() {
			return name;
		}
		public void setAge(int age) {
			this.age = age;
		}
		public void setBreed(String breed) {
			this.breed = breed;
		}
		public void setName(String name) {
			this.name = name;
		}
	}
	
	//����:����һ��������Ϊ����,�����ж��������,����,Ʒ��.������������,��,è,�ϻ�,Ȼ���ӡ
	//����Ϣ,��:2����������������������Ľ� 
	static class animal {
		String name,breed;
		int age;
		animal(String name,String breed,int age){
			this.name=name;
			this.breed=breed;
			this.age=age;
		}
		void bark(){
			
		}
	}
	
	static class Dog extends animal{
		Dog(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"���"+breed+name+"�����Ľ�");
		}
	}
	
	static class Cat extends animal{
		Cat(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"���"+breed+name+"�����Ľ�");
		}
	}
	
	static class Tiger extends animal{
		Tiger(String name, String breed, int age) {
			super(name, breed, age);
			// TODO Auto-generated constructor stub
		}
		void bark(){
			System.out.println(age+"���"+breed+name+"�໵Ľ�");
		}
	}
	
	static void intro(animal a) {
		a.bark();
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		usr u1=new usr();
		u1.setphone("139xxxxx");
		u1.setpassword("123456","sdf");
		System.out.println(u1.getphone());
		
		
		Dog d1=new Dog("���", "����", 5);
		intro(d1);
				
	}

}
