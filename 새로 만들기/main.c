#include <stdio.h>
#include "user.c"

int main(){
	int menu;

	printf("#### 로그인 ####\n");
	printf("1. 회원가입\n");
	printf("2. 로그인\n");
	printf("메뉴를 선택해주세요 : ");
	scanf("%d", &menu);

	if (menu == 1){
		signup();
	} else if (menu == 2){
		login();
	} else {
		printf("잘못된 입력입니다.\n");
	}
	return 0;
}
