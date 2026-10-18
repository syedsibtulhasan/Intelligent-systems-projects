import pandas as pd

data = [
    # Low Severity
    ("Spelling mistake on landing page button label", "Low"),
    ("Footer copyright year shows 2023 instead of current year", "Low"),
    ("Dark mode toggle icon misaligned by 2 pixels in Chrome", "Low"),
    ("Font color on settings modal is light gray, hard to read", "Low"),
    ("Tooltip delay on profile avatar is slightly too long", "Low"),
    ("User dashboard layout padding inconsistent on mobile viewport", "Low"),
    ("Minor text clipping on terms of service text paragraph", "Low"),

    # Medium Severity
    ("Export to CSV fails when filtering more than 500 rows", "Medium"),
    ("Profile image upload takes over 15 seconds to complete", "Medium"),
    ("Search pagination resets to page 1 when sorting columns", "Medium"),
    ("Memory consumption gradually increases during background data sync", "Medium"),
    ("Email notification arrives 10 minutes late for password reset", "Medium"),
    ("PDF report generation throws layout warning on multi-page tables", "Medium"),
    ("Session timeout popup does not refresh token automatically", "Medium"),

    # High Severity
    ("Database connection pool timeout under heavy concurrent load", "High"),
    ("API endpoint returns 500 Internal Server Error on checkout submit", "High"),
    ("JWT auth token expires immediately after login for non-admin users", "High"),
    ("Payment gateway Webhook throws 403 Forbidden on payment confirmation", "High"),
    ("User password hash exposed in debug console logs during registration", "High"),
    ("SQL query error on filter input causing page freeze", "High"),
    ("Third-party OAuth integration fails to redirect back to application", "High"),

    # Critical Severity
    ("Fatal Crash: NullPointerException at AuthManager.java:104 causing server shutdown", "Critical"),
    ("Unhandled Exception in Kernel Driver causing System Blue Screen BSOD", "Critical"),
    ("Database corruption detected on primary transaction table during write operation", "Critical"),
    ("Out of Memory Error: JVM heap space exhausted causing complete service downtime", "Critical"),
    ("Segmentation fault core dumped in C++ backend service", "Critical"),
    ("Ransomware activity detected on file server storage partition", "Critical"),
    ("Infinite loop in main server thread locking CPU at 100% utilization", "Critical")
]

df = pd.DataFrame(data, columns=["description", "severity"])
df.to_csv("bug_reports.csv", index=False)
print("[+] Created dataset 'bug_reports.csv' with", len(df), "sample records.")