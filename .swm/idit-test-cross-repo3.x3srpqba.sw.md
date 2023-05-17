---
id: x3srpqba
title: Idit-test-cross-repo3
file_version: 1.1.2
app_version: 1.8.0
---

This is another doc with snippets from two-three different code files.

<br/>

snippet 1
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/extensions/vscode/src/logger.ts
```typescript
16       const logStream = pino.multistream([
17         // Log to file
18         pino.destination({
19           dest: path.resolve(context.logUri.fsPath, 'swimm.log'),
20           mkdir: true,
21         }),
22     
23         // Log to vscode output panel
24         {
25           write(msg) {
26             vscodeLoggingOutput.append(msg);
27           },
28         },
29       ]);
```

<br/>

snippet 2
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/extensions/vscode/src/welcomePanel.ts
```typescript
94         function sendContextChangedEvent({
95           repoInfo,
96           isNoRepo,
97           isMultiRepo,
98         }: {
99           repoInfo: RepoInfo | null;
100          isNoRepo: boolean;
101          isMultiRepo: boolean;
102        }) {
103          void postMessage({
104            type: 'context-changed',
105            workspaceId: repoInfo?.workspaceId,
106            workspaceName: repoInfo?.workspaceName,
107            isWorkspaceAdmin: repoInfo?.isWorkspaceAdmin ?? false,
108            isExpiredWorkspaceUser: repoInfo?.isExpiredWorkspaceUser ?? false,
109            isExpiredRepo: repoInfo?.isExpiredRepo ?? false,
110            repoId: repoInfo?.repoId,
111            repoPath: repoInfo?.repoPath,
112            repoName: repoInfo?.repoName,
113            repoStatusDetails: repoInfo?.repoStatusDetails,
114            docAmount: repoInfo?.docAmount,
115            isNoRepo,
116            isMultiRepo,
117          });
118        }
```

<br/>

snippet 3
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/extensions/vscode/gulpfile.ts
```typescript
17       const argv = yargs(hideBin(process.argv))
18         .option('pre-release', {
19           boolean: true,
20           description: 'Mark this package as a pre-release',
21         })
22         .parseSync();
```

<br/>

Adding this snippet to see a mixed cross with 2 different docs:

<br/>


<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
<!-- NOTE-swimm-repo ::veezvxCuzpPrRLLXWD2E:: -->
### 📄 ide/extensions/vscode/src/logger.ts
```typescript
51       if (context.extensionMode === vscode.ExtensionMode.Production || process.env.FORCE_SENTRY) {
52         logStream.add(
53           pinoSentry.createWriteStream({
54             dsn: 'https://676f44e29cfd4647b0391a8bf23f0d09@o1000337.ingest.sentry.io/6515757',
55             environment: envConfig.env,
56             release: `swimm-vscode-extension@${process.env.REVISION || 'unknown'}`,
57             level: 'error',
58             stackAttributeKey: 'err.stack',
59             integrations(integrations) {
60               // As we are in a shared process and the VS Code extension host
61               // already handles this, we don't register those integrations to avoid
62               // intefering with it
63               integrations = integrations.filter(
64                 (integration) => !['OnUncaughtException', 'OnUnhandledRejection'].includes(integration.name)
65               );
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://swimm-web-app.web.app/repos/Z2l0aHViJTNBJTNBdGVzdC1naXRodWItYXBwJTNBJTNBc3dpbW1pbw==/docs/x3srpqba).