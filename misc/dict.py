tmp = {"permissions": []}
new_perm_super = {
    "group": "GlobalGroup_MLOps_SuperUser_L2",
    "admin": True,
    "executeApp": True,
    "exportDatasetsData": True,
    "manageAdditionalDashboardUsers": True,
    "manageDashboardAuthorizations": True,
    "manageExposedElements": True,
    "moderateDashboards": True,
    "readDashboards": True,
    "readProjectContent": True,
    "runScenarios": True,
    "shareToWorkspaces": True,
    "writeDashboards": True,
    "writeProjectContent": True,
}
tmp["permissions"].append(new_perm_super)
print(tmp)
