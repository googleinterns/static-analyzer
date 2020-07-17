class Main{
static public void main(String[] args){
    System.out.println("Hello"); 

    int x = 5; 
    String SECRET_KEY = "SHIFTLEFT440PLZCATCH786ME"

    if(x >= 5){
       System.out.println(2+2);
    }
    else if(x < 5){
        System.out.println(2+2); 
    } 

    String SECRET_TOKEN = generateSecretToken()

}  

String generateSecretToken() {
    Random r = new Random();
    return Long.toHexString(r.nextLong());
}

}