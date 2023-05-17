---
id: 1636v
title: doc with cross repo snippets
file_version: 1.1.2
app_version: 1.8.0
---

republish cloud doc is very important function in swimm
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 cloud/shared/cloud-docs.ts
```typescript
22     export async function republishCloudDoc(
23       user: User,
24       workspaceId: string,
25       repoId: string,
26       branch: string,
27       cloudDocId: string,
28       swm: SwmFile
29     ) {
30       const cloudSwm = cloudifySwm(swm);
31       const updateFields = getCloudDocUpdateFields(adminFieldValue, cloudSwm, user, { repoId, branch });
32       await initializedDB
33         .collection(firestoreCollectionNames.WORKSPACES)
34         .doc(workspaceId)
35         .collection(firestoreCollectionNames.CLOUD_DOCS)
36         .doc(cloudDocId)
37         .update(updateFields);
38     }
```

<br/>

another snippet from same file
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 apps/web/src/modules/cloud-docs/cloud-doc-utils.ts
```typescript
34     export async function cloudDocExists(workspaceId: string, cloudDocId: string): Promise<boolean> {
35       const result = await getDocRefFromSubCollection(
36         collectionNames.WORKSPACES,
37         workspaceId,
38         collectionNames.CLOUD_DOCS,
39         cloudDocId
40       );
41       if (result.code !== config.SUCCESS_RETURN_CODE) {
42         throw new Error(
43           `Failed to check whether cloud doc exists, workspaceId: ${workspaceId}, cloudDocId: ${cloudDocId}, error: ${result.errorMessage}`
44         );
45       }
46       return result.data.exists;
47     }
```

<br/>

snippet from indexer
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/server/src/indexer.ts
```typescript
64     export interface IndexedDocumentWithPath {
65       documentPath: string;
66       document: IndexedDocument;
67     }
```

<br/>

two variables to used
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/server/src/indexer.ts
```typescript
162      private readonly _indexedDocuments = new Map<string, IndexedDocument>();
163      private readonly _indexedDocumentsById = new Map<string, IndexedDocumentWithPath>();
164    
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](http://localhost:5000/repos/Z2l0aHViJTNBJTNBdGVzdC1naXRodWItYXBwJTNBJTNBc3dpbW1pbw==/docs/1636v).