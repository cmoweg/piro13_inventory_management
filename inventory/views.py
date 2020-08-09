from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from inventory.forms import ItemForm, AccountForm
from inventory.models import Item, Account


def item_list(request):
    items = Item.objects.all()
    ctx = {
        "items": items
    }
    return render(request, "inventory/item_list.html", ctx)


@require_POST
def amount_ajax(request):
    pk = request.POST.get("pk")
    status = request.POST.get("status")
    item = get_object_or_404(Item, pk=pk)

    if status == "plus":
        item.amount += 1
    else:
        if item.amount > 0:
            item.amount -= 1
        else:
            redirect('inventory:item_list')
    item.save()
    ctx = {
        "amount": item.amount,
    }
    return JsonResponse(ctx)


def item_read(request, pk):
    item = Item.objects.get(pk=pk)
    ctx = {
        "item": item
    }
    return render(request, "inventory/item_detail.html", ctx)


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect("inventory:item_read", item.pk)
    else:
        form = ItemForm()
        ctx = {
            "form": form
        }
        return render(request, "inventory/item_create.html", ctx)


def item_update(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
        return redirect("inventory:item_read", item.pk)

    else:
        form = ItemForm(instance=item)
        ctx = {
            "form": form
        }
        return render(request, "inventory/item_update.html", ctx)


def item_delete(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == "POST":
        item.delete()
        return redirect("inventory:item_list")

    return redirect("inventory:item_read", item.pk)

def account_list(request):
    accounts = Account.objects.all()
    ctx = {
        "accounts": accounts
    }
    return render(request, "inventory/account_list.html", ctx)


def account_read(request, pk):
    account = Account.objects.get(pk=pk)
    ctx = {
        "account": account
    }
    return render(request, "inventory/account_read.html", ctx)


def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save()
            return redirect("inventory:account_read", account.pk)
    else:
        form = AccountForm()
        ctx = {
            "form": form
        }
        return render(request, "inventory/account_create.html", ctx)


def account_update(request, pk):
    account = Account.objects.get(pk=pk)

    if request.method == "POST":
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save()
        return redirect("inventory:account_read", account.pk)

    else:
        form = AccountForm(instance=account)
        ctx = {
            "form": form
        }
        return render(request, "inventory/account_update.html", ctx)


def account_delete(request, pk):
    account = Account.objects.get(pk=pk)

    if request.method == "POST":
        account.delete()
        return redirect("inventory:account_list")

    return redirect("inventory:account_read", account.pk)