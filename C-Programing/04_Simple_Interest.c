int main(){
    float principle,rate,time;
    printf("enter principle:");
    scanf("%f",&principle);
    printf("enter rate:");
    scanf("%f",&rate);
    printf("enter time:");
    scanf("%f",&time);
    float SI =(principle*rate*time)/100;
    printf("simple interest is:%f",SI);
    return 0;
}
