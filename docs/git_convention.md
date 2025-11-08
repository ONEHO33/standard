# Git Convention



## Repository Convention

- 소문자 사용
- '-' 사용

  

## Branch Convention



-   main : 제품으로 출시될 수 있는 브랜치
    -   hotfix : 출시 버전에서 발생한 버그를 수정 하는 브랜치
        -   hotfix-{major-version}.{minor-version}.{patch-version}

-   release : 출시 버전을 준비하는 branch

    - release-{major-version}.{minor-version}

-   develop : 다음 출시 버전을 개발하는 브랜치

    -   feature : 기능을 개발하는 branch in Local

        -   feature/feature/{issue-number}-{feature-name}

        -   feature/{feature-name}

            git  checkout  -b  feature/123-login  develop

            git  checkout  develop

            git  merge  --no-ff  feature/123-login

            git  branch  -d  feature/123-login

-   bugfix/버그번호 : 버그를 수정하는 브랜치

-   test : 테스트를 하는 브랜치

```bash
#--- main branch
#---     version : 1.0 (tag로 지정)
git  checkout  main
git  tag  -a  1.0

#--- hostfix branch
git  checkout  -b  hotfix-1.0.1  main
# 수정 작업

git  checkout  main
git  merge  --no-ff  hotfix-1.0.1
git  tag  -a  1.0.1

git  checkout  develop
git  merge  --no-ff  release-1-1
git  branch  -d  hotfix-1.0.1

#--- release branch
git  checkout  -b  release-1.1  develop
# 보완 작업

git  checkout  main
git  merge  --no-ff  release-1-1
git  tag  -a  1.1

git  checkout  develop
git  merge  --no-ff  release-1-1
git  branch  -d  release-1-1

#--- develop branch
git  checkout  develop

#--- feature branch
#---     Issue number : 123
#---     Feature-name : login
git  checkout  -b  feature/123-login  develop
# 개발 작업

git  checkout  develop
git  merge  --no-ff  feature/123-login
git  branch  -d  feature/123-login
git  push  origin  develop
```

  

## Commit Convention

```bash
{Type: Subject}

{Body}

{Footers}
```

- [Commit Convention](https://velog.io/@archivvonjang/Git-Commit-Message-Convention)
- Type
  - Feature : 새로운 기능
  - Fix : 버그 수정
  - Design : UI 수정
  - !BREAKING CHANGE : API의 커다란 변경
  - !HOTFIX : Hotfix
  - Style : 코드 포맷 변경
  - Refactor : Refactoring
  - Comment : 주석 추가/변경
  - Docs : 문서 수정
  - Test : 테스트 코드
  - Chore : 빌드 업무 수정 등
  - Env : 환경 수정
  - Rename : 이름 변경, 이동 등
  - Remove : 파일을 삭제하는 작업
- Subject
  - 최대 50글자를 넘지 않도록 한다.
  - 마침표를 사용하지 않는다.
  - 영문으로 작성할 경우 첫 글자를 대문자로 표기한다.
  - 동사 원형을 사용한다. ex) Change(O) Changed(X) Changes(X)
  - 명령어 어조(개조식 문장)으로 작성한다.
- Body
  - 한 줄 당 72자를 넘지 않도록 한다.
  - 양에 제한이 없으며, 최대한 상세히 작성한다.
  - 어떻게 가 아닌 무엇을 왜 변경했는지에 대해 작성한다.
- Footers : 여러줄로 작성
  - Resolves: #{해결한 이슈 번호}
  - Fixes: #{수정중인 이슈 번호}
  - Related to: #{관련 이슈 번호1}, #{관련 이슈 번호2}
  - Ref: #{참고 이슈 번호}



## 기타

-   Merge Request > 동료 Review > Merge
-   승인 프로세스
    -   Compare
    -   Create pull request
    -   Reviewer가 승인
    -   Accept

  