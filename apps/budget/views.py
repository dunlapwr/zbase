from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def budget_overview(request):
    """Budget overview — stub for Phase 4."""
    return render(request, "budget/overview.html", {
        "breadcrumbs": [{"label": "Budget", "url": ""}],
    })


@login_required
def budget_transactions(request):
    """Transactions list — stub for Phase 4."""
    return render(request, "budget/transactions.html", {
        "breadcrumbs": [
            {"label": "Budget", "url": "/budget/"},
            {"label": "Transactions", "url": ""},
        ],
    })


@login_required
def budget_accounts(request):
    """Linked accounts — stub for Phase 4."""
    return render(request, "budget/accounts.html", {
        "breadcrumbs": [
            {"label": "Budget", "url": "/budget/"},
            {"label": "Accounts", "url": ""},
        ],
    })
