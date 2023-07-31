from django.http import JsonResponse
from django.shortcuts import render, redirect

from users.decorators import login_required

from users.models import EngineerTB
from .models import BoardTB, UploadFile
from .forms import BoardForm, UploadFileForm


@login_required
def notice(request):
    data = BoardTB.objects.all().order_by("-brd_id")
    user_data = EngineerTB.objects.all()
    return render(request, "board/notice.html", {"data": data, "user_data": user_data})


@login_required
def post(request):
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        file_form = UploadFileForm(request.POST, request.FILES)
        if board_form.is_valid():
            board = board_form.save(commit=False)
            board.engineer = EngineerTB.objects.get(id=request.user.id)
            board.save()

            if file_form.is_valid():
                file = file_form.cleaned_data["file"]
                if file:
                    upload_file = UploadFile(brd_id=board, file=file)
                    upload_file.save()

        else:
            response_data = {"message": "게시글을 게시하는데 실패하였습니다."}
            return JsonResponse(response_data, status=400)

        response_data = {"message": "게시물이 성공적으로 생성되었습니다."}
        return JsonResponse(response_data)

    else:
        board_form = BoardForm()
        file_form = UploadFileForm()
        return render(
            request,
            "board/post.html",
            {"board_form": board_form, "file_form": file_form},
        )


def content(request, brd_id):
    data = BoardTB.objects.all()
    for board in data:
        if board.brd_id == brd_id:
            data = board

    return render(request, "board/content.html", {"data": data})


def board_list(request):
    if request.method == "GET":
        boards = BoardTB.objects.all()
        boards = BoardTB.objects.order_by("-brd_id")  # brd_id 내림차순 정렬
        data = []

        for board in boards:
            board_data = {
                "brd_id": board.brd_id,
                "brd_title": board.brd_title,
                "brd_content": board.brd_content,
                "brd_create": board.brd_create.strftime("%Y-%m-%d %H:%M:%S")
                if board.brd_create
                else None,
                "brd_update": board.brd_update.strftime("%Y-%m-%d %H:%M:%S")
                if board.brd_create
                else None,
            }
            data.append(board_data)

        return JsonResponse(data, safe=False)


def edit(request, brd_id):
    if request.method == "POST":
        # 게시물 정보 가져오기
        board = BoardTB.objects.get(brd_id=brd_id)

        # 게시물 수정 처리
        board_form = BoardForm(request.POST, request.FILES, instance=board)
        if board_form.is_valid():
            board = board_form.save(commit=False)
            board.save()

            # 파일 업로드 처리
            file_form = UploadFileForm(request.POST, request.FILES)
            if file_form.is_valid():
                board.uploadfile_set.all().delete()  # 기존 파일 삭제
                file = file_form.cleaned_data["file"]
                if file:
                    upload_file = UploadFile(brd_id=board, file=file)
                    upload_file.save()

            data = {"message": "게시물이 성공적으로 수정되었습니다."}
            return JsonResponse(data)
        else:
            data = {"message": "게시글을 수정하는데 실패하였습니다."}
            return JsonResponse(data, status=400)
    else:
        board = BoardTB.objects.get(brd_id=brd_id)
        board_form = BoardForm(instance=board)
        file_form = UploadFileForm()
        return render(
            request,
            "board/edit.html",
            {"data": board, "board_form": board_form, "file_form": file_form},
        )


def board_delete(request, brd_id):
    board = BoardTB.objects.get(brd_id=brd_id)
    board.delete()
    return redirect("board:notice")
