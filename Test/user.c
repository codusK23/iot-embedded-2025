#include <stdio.h>
#include <string.h>

void signup()
{
	char id[100];
	char pw[100];

	printf("#### 회원가입 ####\n");
	printf("등록할 아이디를 입력해주세요 : ");
	scanf("%s", id);
	printf("등록할 비밀번호를 입력해주세요 : ");
	scanf("%s", pw);

	FILE *fp = fopen("userFile.txt", "w");

	if (fp == NULL){
		printf("파일 저장실패\n");
		return;
	}

	fprintf(fp, "%s %s\n", id, pw);
	fclose(fp);

	printf("회원가입 완료\n");
}


void login()
{
	char inputId[100];
	char inputPw[100];
	char userId[100];
	char userPw[100];

	printf("#### 로그인 ####\n");
	printf("아이디를 입력해주세요 : ");
	scanf("%s", inputId);
	printf("비밀번호를 입력해주세요 : ");
	scanf("%s", inputPw);

	FILE *fp = fopen("userFile.txt", "r");

	if (fp == NULL){
		printf("회원 정보가 없습니다. 회원가입 먼저  해주세요.\n");
		return;
	}

	fscanf(fp, "%s %s", userId, userPw);
	fclose(fp);

	if (strcmp(inputId, userId) == 0 && strcmp(inputPw, userPw) == 0){
		printf("로그인 완료\n");
	}else {
		printf("로그인 실패 : 아이디 또는 비밀번호가 일치하지 않습니다.\n");
	}
}
