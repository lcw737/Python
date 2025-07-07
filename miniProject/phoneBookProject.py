# ------------------1단계------------------#

# name = input("이름을 입력하세요: ")
# print("내 이름은 ", name)

# phone = input("번호를 입력하세요")
# print("내 번호는:", phone)

# addr = input("주소를 입력하세요")
# print("내 주소는:", addr)

# ------------------2단계------------------#

# contact_list = []

# name = input("내 이름:")
# phone = input("내 번호:")
# addr = input("내 주소:")

# contact = {'이름':name, '번호':phone, '주소':addr}
# contact_list.append(contact)

# print(contact_list)

# ------------------3단계------------------#

# contact_list = []

# for i in range(3):
#   name = input("이름을 입력:")
#   phone = input("번호를 입력:")
#   addr = input("주소를 입력")

#   contact = {'이름':name,'번호':phone,'주소':addr}
#   contact_list.append(contact)

# print(contact_list)

# ------------------4단계------------------#

# contact_list = []

# while True:
#   name = input("이름을 입력:")
#   if name == "끝":
#     break
#   phone = input("번호를 입력")
#   addr = input("주소를 입력:")
#   contact = {'이름':name,'번호':phone,'주소':addr}
#   contact_list.append(contact)

#   for contact in contact_list:
#     print(f"{contact['이름']}\t{contact['번호']}\t{contact['주소']}")

# ------------------5단계------------------#

# contact_list = []

# while True:
#   print("1. 입력 2. 출력 3. 종료 ")
#   choice = input("메뉴를 선택하세요:")
#   if choice == "1":
#     name = input("이름을 입력:")
#     phone = input("번호를 입력:")
#     addr = input("주소를 입력:")
#     print("입력완료!")

#     contact = {'이름':name,'번호':phone,'주소':addr}
#     contact_list.append(contact)

#   elif choice == "2":
#     print("이름\t번호\t주소")
#     for contact in contact_list:
#       print(f"{contact['이름']}\t{contact['번호']}\t{contact['주소']}")

#   elif choice == "3":
#     print("프로그램을 종료합니다")
#     break

#   else:
#     print("잘못된 메뉴입니다. 다시 선택하세요.")

# ------------------6단계------------------#

# contact_list = []

# while True:
#     print("1. 입력 2. 출력 3. 검색 4. 종료 ")
#     choice = input("메뉴를 선택하세요:")
#     if choice == "1":
#         name = input("이름을 입력:")
#         phone = input("번호를 입력:")
#         addr = input("주소를 입력:")
#         print("입력완료!")

#         contact = {'이름': name, '번호': phone, '주소': addr}
#         contact_list.append(contact)

#     elif choice == "2":
#         print("이름\t번호\t주소")
#         for contact in contact_list:
#             print(f"{contact['이름']}\t{contact['번호']}\t{contact['주소']}")

#     elif choice == "3":
#         search_name = input("검색할 이름을 입력하세요:")
#         found = False
#         for contact in contact_list:
#             if contact['이름'] == search_name:
#                 print(
#                     f"이름: {contact['이름']}, 번호: {contact['번호']}, 주소: {contact['주소']}")
#                 found = True
#         if not found:
#             print("찾는사람이 없습니다.")

#     elif choice == "4":
#         print("프로그램을 종료합니다.")
#         break

#     else:
#         print("잘못된 메뉴입니다. 다시 선택하세요.")

# ------------------7단계------------------#

# contact_list = []

# while True:
#     print("1. 입력 2. 출력 3. 검색 4. 수정 5. 종료 ")
#     choice = input("메뉴를 선택하세요:")
#     if choice == "1":
#         name = input("이름을 입력:")
#         phone = input("번호를 입력:")
#         addr = input("주소를 입력:")
#         print("입력완료!")

#         contact = {'이름': name, '번호': phone, '주소': addr}
#         contact_list.append(contact)

#     elif choice == "2":
#         print("이름\t번호\t주소")
#         for contact in contact_list:
#             print(f"{contact['이름']}\t{contact['번호']}\t{contact['주소']}")

#     elif choice == "3":
#         search_name = input("검색할 이름을 입력하세요:")
#         found = False
#         for contact in contact_list:
#             if contact['이름'] == search_name:
#                 print(
#                     f"이름: {contact['이름']}, 번호: {contact['번호']}, 주소: {contact['주소']}")
#                 found = True
#         if not found:
#             print("찾는사람이 없습니다.")

#     elif choice == "4":
#         name_update = input("수정할 이름을 입력하세요:")
#         found = False
#         for contact in contact_list:
#             if contact['이름'] == name_update:
#                 print(
#                     f"이름:{contact['이름']}, 번호:{contact['번호']}, 주소{contact['주소']}")
#                 new_name = input("수정할 이름을 입력하세요:")
#                 new_phone = input("수정할 번호를 입력해주세요:")
#                 new_addr = input("수정할 주소를 입력하세요:")
#                 contact['이름'] = new_name
#                 contact['번호'] = new_phone
#                 contact['주소'] = new_addr
#                 found = True
#         if not found:
#           print("찾는사람이 없습니다.")

#     elif choice == "5":
#         print("프로그램을 종료합니다.")
#         break

#     else:
#         print("잘못된 메뉴입니다. 다시 선택하세요.")

# ------------------8단계------------------#

contact_list = []

while True:
    print("1. 입력 2. 출력 3. 검색 4. 수정 5. 삭제 6. 종료 ")
    choice = input("메뉴를 선택하세요:")
    if choice == "1":
        print(f"{'입력기능':-^30}")
        name = input("이름을 입력:")
        phone = input("번호를 입력:")
        addr = input("주소를 입력:")
        print("입력완료!")

        contact = {'이름': name, '번호': phone, '주소': addr}
        contact_list.append(contact)

    elif choice == "2":
        print(f"{'출력기능':-^30}")
        print("이름\t번호\t주소")
        for contact in contact_list:
            print(f"{contact['이름']}\t{contact['번호']}\t{contact['주소']}")

    elif choice == "3":
        print(f"{'검색기능':-^30}")
        search_name = input("검색할 이름을 입력하세요:")
        found = False
        for contact in contact_list:
            if contact['이름'] == search_name:
                print(
                    f"이름: {contact['이름']}, 번호: {contact['번호']}, 주소: {contact['주소']}")
                found = True
        if not found:
            print("찾는사람이 없습니다.")

    elif choice == "4":
        print(f"{'수정기능':-^30}")
        name_update = input("수정할 이름을 입력하세요:")
        found = False
        for contact in contact_list:
            if contact['이름'] == name_update:
                print(
                    f"이름:{contact['이름']}, 번호:{contact['번호']}, 주소{contact['주소']}")
                new_name = input("수정할 이름을 입력하세요:")
                new_phone = input("수정할 번호를 입력해주세요:")
                new_addr = input("수정할 주소를 입력하세요:")
                contact['이름'] = new_name
                contact['번호'] = new_phone
                contact['주소'] = new_addr
                found = True
                print("연락처가 수정되었습니다.")
        if not found:
            print("찾는사람이 없습니다.")

    elif choice == "5":
        print(f"{'삭제기능':-^30}")
        name_delete = input("삭제할 이름을 입력하세요:")
        found = False
        for i, contact in enumerate(contact_list):
            if contact['이름'] == name_delete:
                del contact_list[i]
                print("연락처가 삭제되었습니다.")
                found = True
                break
            if not found:
                print("찾는사람이 없습니다.")

    elif choice == "6":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 메뉴입니다. 다시 선택하세요.")
