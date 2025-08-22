# 修复建议

## src/components/ClaudeCodeSession.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 138 行:
```typescript
// 原来: useComponentMetrics('ClaudeCodeSession');
// 修改为: useComponentMetrics(t("category.claudecodesession"));
```

第 334 行:
```typescript
// 原来: setError("Failed to load session history");
// 修改为: setError(t("category.failedToLoadSessionHistory"));
```

第 346 行:
```typescript
// 原来: if ('process_type' in s && s.process_type && 'ClaudeSession' in s.process_type) {
// 修改为: if ('process_type' in s && s.process_type && t("category.claudesession") in s.process_type) {
```

第 437 行:
```typescript
// 原来: setError("Please select a project directory first");
// 修改为: setError(t("category.pleaseSelectAProjectDirectoryFirst"));
```

第 595 行:
```typescript
// 原来: context: `Tool execution failed`,
// 修改为: context: `Tool execution failed`,
```

第 817 行:
```typescript
// 原来: setError("Failed to send prompt");
// 修改为: setError(t("category.failedToSendPrompt"));
```

第 994 行:
```typescript
// 原来: result: "Session cancelled by user",
// 修改为: result: t("category.sessionCancelledByUser"),
```

第 1006 行:
```typescript
// 原来: result: `Failed to cancel execution: ${err instanceof Error ? err.message : 'Unknown error'}. The process may still be running in the background.`,
// 修改为: result: `Failed to cancel execution: ${err instanceof Error ? err.message : t("category.unknownError")}. The process may still be running in the background.`,
```

第 1055 行:
```typescript
// 原来: setError("Failed to fork checkpoint");
// 修改为: setError(t("category.failedToForkCheckpoint"));
```

第 1306 行:
```typescript
// 原来: <TooltipSimple content={queuedPromptsCollapsed ? "Expand queue" : "Collapse queue"} side="top">
// 修改为: <TooltipSimple content={queuedPromptsCollapsed ? t("category.expandQueue") : "Collapse queue"} side="top">
```

第 1306 行:
```typescript
// 原来: <TooltipSimple content={queuedPromptsCollapsed ? "Expand queue" : "Collapse queue"} side="top">
// 修改为: <TooltipSimple content={queuedPromptsCollapsed ? "Expand queue" : t("category.collapseQueue")} side="top">
```

第 1330 行:
```typescript
// 原来: {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
// 修改为: {queuedPrompt.model === "opus" ? t("category.opus") : "Sonnet"}
```

第 1330 行:
```typescript
// 原来: {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
// 修改为: {queuedPrompt.model === "opus" ? "Opus" : t("category.sonnet")}
```

第 1365 行:
```typescript
// 原来: <TooltipSimple content="Scroll to top" side="top">
// 修改为: <TooltipSimple content=t("category.scrollToTop") side="top">
```

第 1403 行:
```typescript
// 原来: <TooltipSimple content="Scroll to bottom" side="top">
// 修改为: <TooltipSimple content=t("category.scrollToBottom") side="top">
```

第 1448 行:
```typescript
// 原来: <TooltipSimple content="Session Timeline" side="top">
// 修改为: <TooltipSimple content=t("category.sessionTimeline") side="top">
```

第 1467 行:
```typescript
// 原来: <TooltipSimple content="Copy conversation" side="top">
// 修改为: <TooltipSimple content=t("category.copyConversation") side="top">
```

第 1508 行:
```typescript
// 原来: <TooltipSimple content="Checkpoint Settings" side="top">
// 修改为: <TooltipSimple content=t("category.checkpointSettings") side="top">
```

第 1598 行:
```typescript
// 原来: <DialogTitle>Fork Session</DialogTitle>
// 修改为: <DialogTitle>Fork Session</DialogTitle>
```

第 1606 行:
```typescript
// 原来: <Label htmlFor="fork-name">New Session Name</Label>
// 修改为: <Label htmlFor="fork-name">New Session Name</Label>
```

第 1613 行:
```typescript
// 原来: if (e.key === "Enter" && !isLoading) {
// 修改为: if (e.key === t("category.enter") && !isLoading) {
```

第 1658 行:
```typescript
// 原来: <DialogTitle>Slash Commands</DialogTitle>
// 修改为: <DialogTitle>Slash Commands</DialogTitle>
```

## src/components/TabManager.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 105 行:
```typescript
// 原来: title="Unsaved changes"
// 修改为: title=t("category.unsavedChanges")
```

第 323 行:
```typescript
// 原来: title="Scroll tabs left"
// 修改为: title=t("category.scrollTabsLeft")
```

第 372 行:
```typescript
// 原来: title={canAddTab() ? "New project (Ctrl+T)" : "Maximum tabs reached"}
// 修改为: title={canAddTab() ? "New project (Ctrl+T)" : t("category.maximumTabsReached")}
```

第 397 行:
```typescript
// 原来: title="Scroll tabs right"
// 修改为: title=t("category.scrollTabsRight")
```

## src/components/RunningClaudeSessions.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 47 行:
```typescript
// 原来: setError("Failed to load running sessions");
// 修改为: setError(t("category.failedToLoadRunningSessions"));
```

第 55 行:
```typescript
// 原来: if ('ClaudeSession' in processInfo.process_type) {
// 修改为: if (t("category.claudesession") in processInfo.process_type) {
```

第 111 行:
```typescript
// 原来: const sessionId = 'ClaudeSession' in session.process_type
// 修改为: const sessionId = t("category.claudesession") in session.process_type
```

## src/components/NFOCredits.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 91 行:
```typescript
// 原来: { type: "credit", role: "POWERED BY", name: "Anthropic Claude 4" },
// 修改为: { type: "credit", role: t("category.poweredBy"), name: "Anthropic Claude 4" },
```

第 92 行:
```typescript
// 原来: { type: "credit", role: "CLAUDE CODE", name: "The Ultimate Coding Assistant" },
// 修改为: { type: "credit", role: t("category.claudeCode"), name: "The Ultimate Coding Assistant" },
```

第 92 行:
```typescript
// 原来: { type: "credit", role: "CLAUDE CODE", name: "The Ultimate Coding Assistant" },
// 修改为: { type: "credit", role: "CLAUDE CODE", name: t("category.theUltimateCodingAssistant") },
```

第 93 行:
```typescript
// 原来: { type: "credit", role: "MCP PROTOCOL", name: "Model Context Protocol" },
// 修改为: { type: "credit", role: t("category.mcpProtocol"), name: "Model Context Protocol" },
```

第 93 行:
```typescript
// 原来: { type: "credit", role: "MCP PROTOCOL", name: "Model Context Protocol" },
// 修改为: { type: "credit", role: "MCP PROTOCOL", name: t("category.modelContextProtocol") },
```

第 96 行:
```typescript
// 原来: { type: "credit", role: "RUNTIME", name: "Tauri Framework" },
// 修改为: { type: "credit", role: "RUNTIME", name: t("category.tauriFramework") },
```

第 97 行:
```typescript
// 原来: { type: "credit", role: "UI FRAMEWORK", name: "React + TypeScript" },
// 修改为: { type: "credit", role: t("category.uiFramework"), name: "React + TypeScript" },
```

第 99 行:
```typescript
// 原来: { type: "credit", role: "ANIMATIONS", name: "Framer Motion" },
// 修改为: { type: "credit", role: "ANIMATIONS", name: t("category.framerMotion") },
```

第 100 行:
```typescript
// 原来: { type: "credit", role: "BUILD TOOL", name: "Vite" },
// 修改为: { type: "credit", role: t("category.buildTool"), name: "Vite" },
```

第 100 行:
```typescript
// 原来: { type: "credit", role: "BUILD TOOL", name: "Vite" },
// 修改为: { type: "credit", role: "BUILD TOOL", name: t("category.vite") },
```

第 101 行:
```typescript
// 原来: { type: "credit", role: "PACKAGE MANAGER", name: "Bun" },
// 修改为: { type: "credit", role: t("category.packageManager"), name: "Bun" },
```

第 104 行:
```typescript
// 原来: { type: "text", content: "To the open source community" },
// 修改为: { type: "text", content: t("category.toTheOpenSourceCommunity") },
```

第 105 行:
```typescript
// 原来: { type: "text", content: "To all the beta testers" },
// 修改为: { type: "text", content: t("category.toAllTheBetaTesters") },
```

第 106 行:
```typescript
// 原来: { type: "text", content: "To everyone who believed in this project" },
// 修改为: { type: "text", content: t("category.toEveryoneWhoBelievedInThisProject") },
```

第 162 行:
```typescript
// 原来: title="File a bug"
// 修改为: title=t("category.fileABug")
```

第 205 行:
```typescript
// 原来: alt="Asterisk"
// 修改为: alt=t("category.asterisk")
```

## src/components/AgentExecutionDemo.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 22 行:
```typescript
// 原来: summary: "JSONL Viewer Model Configuration and Setup",
// 修改为: summary: t("category.jsonlViewerModelConfigurationAndSetup"),
```

第 32 行:
```typescript
// 原来: name: "Edit",
// 修改为: name: t("category.edit"),
```

第 93 行:
```typescript
// 原来: name: "Write",
// 修改为: name: t("category.write"),
```

第 104 行:
```typescript
// 原来: font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
// 修改为: font-family: -apple-system, BlinkMacSystemFont, t("category.segoeUi"), Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
```

## src/components/AgentRunOutputViewer.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 109 行:
```typescript
// 原来: updateTabTitle(tabId, `Agent: ${agentRun.agent_name || 'Unknown'}`);
// 修改为: updateTabTitle(tabId, `Agent: ${agentRun.agent_name || t("category.unknown")}`);
```

第 417 行:
```typescript
// 原来: result: "Execution stopped by user",
// 修改为: result: t("category.executionStoppedByUser"),
```

第 438 行:
```typescript
// 原来: message: `Failed to stop execution: ${err instanceof Error ? err.message : 'Unknown error'}`,
// 修改为: message: `Failed to stop execution: ${err instanceof Error ? err.message : t("category.unknownError")}`,
```

第 634 行:
```typescript
// 原来: title={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
// 修改为: title={isFullscreen ? t("category.exitFullscreen") : "Enter fullscreen"}
```

第 634 行:
```typescript
// 原来: title={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
// 修改为: title={isFullscreen ? "Exit fullscreen" : t("category.enterFullscreen")}
```

第 648 行:
```typescript
// 原来: title="Refresh output"
// 修改为: title=t("category.refreshOutput")
```

第 659 行:
```typescript
// 原来: title="Stop execution"
// 修改为: title=t("category.stopExecution")
```

第 678 行:
```typescript
// 原来: <p>No output available yet</p>
// 修改为: <p>No output available yet</p>
```

## src/components/Agents.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 125 行:
```typescript
// 原来: { name: 'JSON Files', extensions: ['json'] },
// 修改为: { name: t("category.jsonFiles"), extensions: ['json'] },
```

第 126 行:
```typescript
// 原来: { name: 'All Files', extensions: ['*'] }
// 修改为: { name: t("category.allFiles"), extensions: ['*'] }
```

第 150 行:
```typescript
// 原来: { name: 'JSON Files', extensions: ['json'] }
// 修改为: { name: t("category.jsonFiles"), extensions: ['json'] }
```

## src/components/ClaudeCodeSession.refactored.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 98 行:
```typescript
// 原来: title: "Select Project Directory"
// 修改为: title: t("category.selectProjectDirectory")
```

第 130 行:
```typescript
// 原来: setError(error instanceof Error ? error.message : "Failed to send prompt");
// 修改为: setError(error instanceof Error ? error.message : t("category.failedToSendPrompt"));
```

第 368 行:
```typescript
// 原来: <DialogTitle>Fork Session from Checkpoint</DialogTitle>
// 修改为: <DialogTitle>Fork Session from Checkpoint</DialogTitle>
```

第 375 行:
```typescript
// 原来: <Label htmlFor="fork-name">New Session Name</Label>
// 修改为: <Label htmlFor="fork-name">New Session Name</Label>
```

第 380 行:
```typescript
// 原来: placeholder="Enter a name for the forked session"
// 修改为: placeholder=t("category.enterANameForTheForkedSession")
```

## src/components/StartupIntro.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 70 行:
```typescript
// 原来: alt="Claudia"
// 修改为: alt=t("category.claudia")
```

## src/components/SlashCommandPicker.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 170 行:
```typescript
// 原来: case 'Escape':
// 修改为: case t("category.escape"):
```

第 175 行:
```typescript
// 原来: case 'Enter':
// 修改为: case t("category.enter"):
```

第 188 行:
```typescript
// 原来: case 'ArrowUp':
// 修改为: case t("category.arrowup"):
```

第 193 行:
```typescript
// 原来: case 'ArrowDown':
// 修改为: case t("category.arrowdown"):
```

第 224 行:
```typescript
// 原来: setError(err instanceof Error ? err.message : 'Failed to load commands');
// 修改为: setError(err instanceof Error ? err.message : t("category.failedToLoadCommands"));
```

第 244 行:
```typescript
// 原来: key = cmd.namespace ? `User Commands: ${cmd.namespace}` : "User Commands";
// 修改为: key = cmd.namespace ? `User Commands: ${cmd.namespace}` : t("category.userCommands");
```

第 246 行:
```typescript
// 原来: key = cmd.namespace ? `Project Commands: ${cmd.namespace}` : "Project Commands";
// 修改为: key = cmd.namespace ? `Project Commands: ${cmd.namespace}` : t("category.projectCommands");
```

第 248 行:
```typescript
// 原来: key = cmd.namespace || "Commands";
// 修改为: key = cmd.namespace || t("category.commands");
```

第 302 行:
```typescript
// 原来: <TabsTrigger value="default">Default</TabsTrigger>
// 修改为: <TabsTrigger value="default">Default</TabsTrigger>
```

第 303 行:
```typescript
// 原来: <TabsTrigger value="custom">Custom</TabsTrigger>
// 修改为: <TabsTrigger value="custom">Custom</TabsTrigger>
```

第 333 行:
```typescript
// 原来: {searchQuery ? 'No commands found' : 'No default commands available'}
// 修改为: {searchQuery ? t("category.noCommandsFound") : 'No default commands available'}
```

第 333 行:
```typescript
// 原来: {searchQuery ? 'No commands found' : 'No default commands available'}
// 修改为: {searchQuery ? 'No commands found' : t("category.noDefaultCommandsAvailable")}
```

第 395 行:
```typescript
// 原来: {searchQuery ? 'No commands found' : 'No custom commands available'}
// 修改为: {searchQuery ? t("category.noCommandsFound") : 'No custom commands available'}
```

第 395 行:
```typescript
// 原来: {searchQuery ? 'No commands found' : 'No custom commands available'}
// 修改为: {searchQuery ? 'No commands found' : t("category.noCustomCommandsAvailable")}
```

## src/components/TimelineNavigator.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 93 行:
```typescript
// 原来: setError("Failed to load timeline");
// 修改为: setError(t("category.failedToLoadTimeline"));
```

第 146 行:
```typescript
// 原来: setError("Failed to create checkpoint");
// 修改为: setError(t("category.failedToCreateCheckpoint"));
```

第 186 行:
```typescript
// 原来: setError("Failed to restore checkpoint");
// 修改为: setError(t("category.failedToRestoreCheckpoint"));
```

第 218 行:
```typescript
// 原来: setError("Failed to compare checkpoints");
// 修改为: setError(t("category.failedToCompareCheckpoints"));
```

第 310 行:
```typescript
// 原来: {node.checkpoint.metadata.userPrompt || "No prompt"}
// 修改为: {node.checkpoint.metadata.userPrompt || t("category.noPrompt")}
```

第 342 行:
```typescript
// 原来: <TooltipContent>Restore to this checkpoint</TooltipContent>
// 修改为: <TooltipContent>Restore to this checkpoint</TooltipContent>
```

第 361 行:
```typescript
// 原来: <TooltipContent>Fork from this checkpoint</TooltipContent>
// 修改为: <TooltipContent>Fork from this checkpoint</TooltipContent>
```

第 380 行:
```typescript
// 原来: <TooltipContent>Compare with another checkpoint</TooltipContent>
// 修改为: <TooltipContent>Compare with another checkpoint</TooltipContent>
```

第 462 行:
```typescript
// 原来: {isLoading ? "Loading timeline..." : "No checkpoints yet"}
// 修改为: {isLoading ? "Loading timeline..." : t("category.noCheckpointsYet")}
```

第 470 行:
```typescript
// 原来: <DialogTitle>Create Checkpoint</DialogTitle>
// 修改为: <DialogTitle>Create Checkpoint</DialogTitle>
```

第 485 行:
```typescript
// 原来: if (e.key === "Enter" && !isLoading) {
// 修改为: if (e.key === t("category.enter") && !isLoading) {
```

第 515 行:
```typescript
// 原来: <DialogTitle>Checkpoint Comparison</DialogTitle>
// 修改为: <DialogTitle>Checkpoint Comparison</DialogTitle>
```

## src/components/ClaudeVersionSelector.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 100 行:
```typescript
// 原来: setError(err instanceof Error ? err.message : "Failed to load Claude installations");
// 修改为: setError(err instanceof Error ? err.message : t("category.failedToLoadClaudeInstallations"));
```

第 116 行:
```typescript
// 原来: case "System":
// 修改为: case t("category.system"):
```

第 118 行:
```typescript
// 原来: case "Custom":
// 修改为: case t("category.custom"):
```

第 127 行:
```typescript
// 原来: case "System":
// 修改为: case t("category.system"):
```

第 129 行:
```typescript
// 原来: case "Custom":
// 修改为: case t("category.custom"):
```

第 150 行:
```typescript
// 原来: <CardTitle>Claude Code Installation</CardTitle>
// 修改为: <CardTitle>Claude Code Installation</CardTitle>
```

第 179 行:
```typescript
// 原来: <CardTitle>Claude Code Installation</CardTitle>
// 修改为: <CardTitle>Claude Code Installation</CardTitle>
```

第 180 行:
```typescript
// 原来: <CardDescription>Error loading installations</CardDescription>
// 修改为: <CardDescription>Error loading installations</CardDescription>
```

第 192 行:
```typescript
// 原来: const systemInstallations = installations.filter(i => i.installation_type === "System");
// 修改为: const systemInstallations = installations.filter(i => i.installation_type === t("category.system"));
```

第 193 行:
```typescript
// 原来: const customInstallations = installations.filter(i => i.installation_type === "Custom");
// 修改为: const customInstallations = installations.filter(i => i.installation_type === t("category.custom"));
```

第 215 行:
```typescript
// 原来: <SelectValue placeholder="Choose Claude installation">
// 修改为: <SelectValue placeholder=t("category.chooseClaudeInstallation")>
```

第 241 行:
```typescript
// 原来: <span>{installation.version || "Unknown version"}</span>
// 修改为: <span>{installation.version || t("category.unknownVersion")}</span>
```

第 287 行:
```typescript
// 原来: <SelectValue placeholder="Select Claude installation">
// 修改为: <SelectValue placeholder=t("category.selectClaudeInstallation")>
```

第 310 行:
```typescript
// 原来: {installation.version || "Version unknown"} • {installation.source}
// 修改为: {installation.version || t("category.versionUnknown")} • {installation.source}
```

第 332 行:
```typescript
// 原来: {installation.version || "Version unknown"} • {installation.source}
// 修改为: {installation.version || t("category.versionUnknown")} • {installation.source}
```

第 373 行:
```typescript
// 原来: {isSaving ? "Saving..." : "Save Selection"}
// 修改为: {isSaving ? "Saving..." : t("category.saveSelection")}
```

## src/components/ClaudeBinaryDialog.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 55 行:
```typescript
// 原来: onError(error instanceof Error ? error.message : "Failed to save Claude binary path");
// 修改为: onError(error instanceof Error ? error.message : t("category.failedToSaveClaudeBinaryPath"));
```

## src/components/AnalyticsErrorBoundary.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 31 行:
```typescript
// 原来: error_type: error.name || 'UnknownError',
// 修改为: error_type: error.name || t("category.unknownerror"),
```

## src/components/PreviewPromptDialog.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 82 行:
```typescript
// 原来: {isLocalhost ? 'Local Development Server' : 'External URL'}
// 修改为: {isLocalhost ? t("category.localDevelopmentServer") : 'External URL'}
```

第 82 行:
```typescript
// 原来: {isLocalhost ? 'Local Development Server' : 'External URL'}
// 修改为: {isLocalhost ? 'Local Development Server' : t("category.externalUrl")}
```

## src/components/ProxySettings.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 52 行:
```typescript
// 原来: message: 'Failed to save proxy settings',
// 修改为: message: t("category.failedToSaveProxySettings"),
```

第 75 行:
```typescript
// 原来: message: 'Failed to load proxy settings',
// 修改为: message: t("category.failedToLoadProxySettings"),
```

第 101 行:
```typescript
// 原来: <Label htmlFor="proxy-enabled">Enable Proxy</Label>
// 修改为: <Label htmlFor="proxy-enabled">Enable Proxy</Label>
```

第 115 行:
```typescript
// 原来: <Label htmlFor="http-proxy">HTTP Proxy</Label>
// 修改为: <Label htmlFor="http-proxy">HTTP Proxy</Label>
```

第 126 行:
```typescript
// 原来: <Label htmlFor="https-proxy">HTTPS Proxy</Label>
// 修改为: <Label htmlFor="https-proxy">HTTPS Proxy</Label>
```

第 137 行:
```typescript
// 原来: <Label htmlFor="no-proxy">No Proxy</Label>
// 修改为: <Label htmlFor="no-proxy">No Proxy</Label>
```

## src/components/FloatingPromptInput.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 189 行:
```typescript
// 原来: description: "Deeper analysis",
// 修改为: description: t("category.deeperAnalysis"),
```

第 198 行:
```typescript
// 原来: name: "Think Harder",
// 修改为: name: t("category.thinkHarder"),
```

第 199 行:
```typescript
// 原来: description: "Extensive reasoning",
// 修改为: description: t("category.extensiveReasoning"),
```

第 654 行:
```typescript
// 原来: if (showFilePicker && e.key === 'Escape') {
// 修改为: if (showFilePicker && e.key === t("category.escape")) {
```

第 661 行:
```typescript
// 原来: if (showSlashCommandPicker && e.key === 'Escape') {
// 修改为: if (showSlashCommandPicker && e.key === t("category.escape")) {
```

第 675 行:
```typescript
// 原来: if (e.key === "Enter" && !e.shiftKey && !isExpanded && !showFilePicker && !showSlashCommandPicker) {
// 修改为: if (e.key === t("category.enter") && !e.shiftKey && !isExpanded && !showFilePicker && !showSlashCommandPicker) {
```

第 800 行:
```typescript
// 原来: <TooltipSimple content="Minimize" side="bottom">
// 修改为: <TooltipSimple content=t("category.minimize") side="bottom">
```

第 960 行:
```typescript
// 原来: <TooltipSimple content="Send message" side="top">
// 修改为: <TooltipSimple content=t("category.sendMessage") side="top">
```

第 1186 行:
```typescript
// 原来: <TooltipSimple content={isLoading ? "Stop generation" : "Send message (Enter)"} side="top">
// 修改为: <TooltipSimple content={isLoading ? t("category.stopGeneration") : "Send message (Enter)"} side="top">
```

第 1256 行:
```typescript
// 原来: FloatingPromptInput.displayName = 'FloatingPromptInput';
// 修改为: FloatingPromptInput.displayName = t("category.floatingpromptinput");
```

## src/components/StorageTab.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 578 行:
```typescript
// 原来: <DialogTitle>Edit Row</DialogTitle>
// 修改为: <DialogTitle>Edit Row</DialogTitle>
```

第 655 行:
```typescript
// 原来: <DialogTitle>New Row</DialogTitle>
// 修改为: <DialogTitle>New Row</DialogTitle>
```

第 729 行:
```typescript
// 原来: <DialogTitle>Delete Row</DialogTitle>
// 修改为: <DialogTitle>Delete Row</DialogTitle>
```

第 776 行:
```typescript
// 原来: <DialogTitle>Reset Database</DialogTitle>
// 修改为: <DialogTitle>Reset Database</DialogTitle>
```

第 816 行:
```typescript
// 原来: <DialogTitle>SQL Query Editor</DialogTitle>
// 修改为: <DialogTitle>SQL Query Editor</DialogTitle>
```

第 823 行:
```typescript
// 原来: <Label htmlFor="sql-query">SQL Query</Label>
// 修改为: <Label htmlFor="sql-query">SQL Query</Label>
```

## src/components/UsageDashboard.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 647 行:
```typescript
// 原来: <span>Daily Usage</span>
// 修改为: <span>Daily Usage</span>
```

## src/components/AgentRunView.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 239 行:
```typescript
// 原来: <Button onClick={onBack}>Go Back</Button>
// 修改为: <Button onClick={onBack}>Go Back</Button>
```

## src/components/AgentsModal.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 232 行:
```typescript
// 原来: <TabsTrigger value="agents">Available Agents</TabsTrigger>
// 修改为: <TabsTrigger value="agents">Available Agents</TabsTrigger>
```

第 412 行:
```typescript
// 原来: <DialogTitle>Delete Agent</DialogTitle>
// 修改为: <DialogTitle>Delete Agent</DialogTitle>
```

## src/components/SessionList.optimized.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 30 行:
```typescript
// 原来: if (!timestamp) return "Unknown time";
// 修改为: if (!timestamp) return t("category.unknownTime");
```

第 102 行:
```typescript
// 原来: SessionCard.displayName = 'SessionCard';
// 修改为: SessionCard.displayName = t("category.sessioncard");
```

## src/components/CreateAgent.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 141 行:
```typescript
// 原来: title="Back to Agents"
// 修改为: title=t("category.backToAgents")
```

## src/components/TabContent.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 92 行:
```typescript
// 原来: title: 'Select Project Folder',
// 修改为: title: t("category.selectProjectFolder"),
```

第 106 行:
```typescript
// 原来: setError('Failed to open folder picker');
// 修改为: setError(t("category.failedToOpenFolderPicker"));
```

第 124 行:
```typescript
// 原来: title: 'New Session',
// 修改为: title: t("category.newSession"),
```

第 159 行:
```typescript
// 原来: title: 'Projects'
// 修改为: title: t("category.projects")
```

第 163 行:
```typescript
// 原来: title="Back to Projects"
// 修改为: title=t("category.backToProjects")
```

第 258 行:
```typescript
// 原来: title: 'Projects',
// 修改为: title: t("category.projects"),
```

## src/components/AgentRunsList.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 174 行:
```typescript
// 原来: {run.status === "completed" ? "Completed" :
// 修改为: {run.status === "completed" ? t("category.completed") :
```

第 175 行:
```typescript
// 原来: run.status === "running" ? "Running" :
// 修改为: run.status === "running" ? t("category.running") :
```

第 176 行:
```typescript
// 原来: run.status === "failed" ? "Failed" :
// 修改为: run.status === "failed" ? t("category.failed") :
```

第 177 行:
```typescript
// 原来: "Pending"}
// 修改为: t("category.pending")}
```

## src/components/FilePicker.optimized.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 140 行:
```typescript
// 原来: setError(err instanceof Error ? err.message : 'Failed to load directory');
// 修改为: setError(err instanceof Error ? err.message : t("category.failedToLoadDirectory"));
```

第 168 行:
```typescript
// 原来: setError(err instanceof Error ? err.message : 'Search failed');
// 修改为: setError(err instanceof Error ? err.message : t("category.searchFailed"));
```

第 197 行:
```typescript
// 原来: case 'ArrowUp':
// 修改为: case t("category.arrowup"):
```

第 201 行:
```typescript
// 原来: case 'ArrowDown':
// 修改为: case t("category.arrowdown"):
```

第 205 行:
```typescript
// 原来: case 'Enter':
// 修改为: case t("category.enter"):
```

第 216 行:
```typescript
// 原来: case 'Escape':
// 修改为: case t("category.escape"):
```

第 335 行:
```typescript
// 原来: {searchQuery.trim() ? 'No files found' : 'Empty directory'}
// 修改为: {searchQuery.trim() ? t("category.noFilesFound") : 'Empty directory'}
```

第 335 行:
```typescript
// 原来: {searchQuery.trim() ? 'No files found' : 'Empty directory'}
// 修改为: {searchQuery.trim() ? 'No files found' : t("category.emptyDirectory")}
```

第 375 行:
```typescript
// 原来: title={entry.is_directory ? "Click to select • Double-click to enter" : "Click to select"}
// 修改为: title={entry.is_directory ? "Click to select • Double-click to enter" : t("category.clickToSelect")}
```

## src/components/WebviewPreview.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 83 行:
```typescript
// 原来: if (e.key === 'Escape' && isMaximized && onToggleMaximize) {
// 修改为: if (e.key === t("category.escape") && isMaximized && onToggleMaximize) {
```

第 135 行:
```typescript
// 原来: setErrorMessage("Invalid URL");
// 修改为: setErrorMessage(t("category.invalidUrl"));
```

第 146 行:
```typescript
// 原来: if (e.key === 'Enter') {
// 修改为: if (e.key === t("category.enter")) {
```

第 210 行:
```typescript
// 原来: {isMaximized ? "Exit full screen (ESC)" : "Enter full screen"}
// 修改为: {isMaximized ? "Exit full screen (ESC)" : t("category.enterFullScreen")}
```

第 327 行:
```typescript
// 原来: title="Preview"
// 修改为: title=t("category.preview")
```

第 344 行:
```typescript
// 原来: <span>Try entering</span>
// 修改为: <span>Try entering</span>
```

## src/components/Topbar.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 70 行:
```typescript
// 原来: if (!status.is_installed && status.output.includes("No such file or directory")) {
// 修改为: if (!status.is_installed && status.output.includes(t("category.noSuchFileOrDirectory"))) {
```

第 78 行:
```typescript
// 原来: output: "Failed to check version",
// 修改为: output: t("category.failedToCheckVersion"),
```

第 116 行:
```typescript
// 原来: : "Claude Code"}
// 修改为: : t("category.claudeCode")}
```

第 148 行:
```typescript
// 原来: <span>Install Claude Code</span>
// 修改为: <span>Install Claude Code</span>
```

## src/components/AgentExecution.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 107 行:
```typescript
// 原来: useComponentMetrics('AgentExecution');
// 修改为: useComponentMetrics(t("category.agentexecution"));
```

第 713 行:
```typescript
// 原来: if (e.key === "Enter" && !isRunning && projectPath && task.trim()) {
// 修改为: if (e.key === t("category.enter") && !isRunning && projectPath && task.trim()) {
```

## src/components/ToolWidgets.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 518 行:
```typescript
// 原来: {filePath || "File content"}
// 修改为: {filePath || t("category.fileContent")}
```

第 1226 行:
```typescript
// 原来: if (line.includes('The file') && line.includes('has been updated')) {
// 修改为: if (line.includes(t("category.theFile")) && line.includes('has been updated')) {
```

第 2050 行:
```typescript
// 原来: <span>Task Instructions</span>
// 修改为: <span>Task Instructions</span>
```

第 2412 行:
```typescript
// 原来: <span>Analysis Prompt</span>
// 修改为: <span>Analysis Prompt</span>
```

## src/components/HooksEditor.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 86 行:
```typescript
// 原来: label: 'Pre Tool Use',
// 修改为: label: t("category.preToolUse"),
```

第 91 行:
```typescript
// 原来: label: 'Post Tool Use',
// 修改为: label: t("category.postToolUse"),
```

第 92 行:
```typescript
// 原来: description: 'Runs after successful tool completion',
// 修改为: description: t("category.runsAfterSuccessfulToolCompletion"),
```

第 96 行:
```typescript
// 原来: label: 'Notification',
// 修改为: label: t("category.notification"),
```

第 97 行:
```typescript
// 原来: description: 'Customizes notifications when Claude needs attention',
// 修改为: description: t("category.customizesNotificationsWhenClaudeNeedsAttention"),
```

第 101 行:
```typescript
// 原来: label: 'Stop',
// 修改为: label: t("category.stop"),
```

第 102 行:
```typescript
// 原来: description: 'Runs when Claude finishes responding',
// 修改为: description: t("category.runsWhenClaudeFinishesResponding"),
```

第 106 行:
```typescript
// 原来: label: 'Subagent Stop',
// 修改为: label: t("category.subagentStop"),
```

第 153 行:
```typescript
// 原来: const [selectedEvent, setSelectedEvent] = useState<HookEvent>('PreToolUse');
// 修改为: const [selectedEvent, setSelectedEvent] = useState<HookEvent>(t("category.pretooluse"));
```

第 165 行:
```typescript
// 原来: const matcherEvents = ['PreToolUse', 'PostToolUse'] as const;
// 修改为: const matcherEvents = [t("category.pretooluse"), 'PostToolUse'] as const;
```

第 165 行:
```typescript
// 原来: const matcherEvents = ['PreToolUse', 'PostToolUse'] as const;
// 修改为: const matcherEvents = ['PreToolUse', t("category.posttooluse")] as const;
```

第 167 行:
```typescript
// 原来: const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
// 修改为: const directEvents = [t("category.notification"), 'Stop', 'SubagentStop'] as const;
```

第 167 行:
```typescript
// 原来: const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
// 修改为: const directEvents = ['Notification', t("category.stop"), 'SubagentStop'] as const;
```

第 167 行:
```typescript
// 原来: const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
// 修改为: const directEvents = ['Notification', 'Stop', t("category.subagentstop")] as const;
```

第 379 行:
```typescript
// 原来: [event]: [...(prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
// 修改为: [event]: [...(prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
```

第 379 行:
```typescript
// 原来: [event]: [...(prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
// 修改为: [event]: [...(prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]), newMatcher]
```

第 395 行:
```typescript
// 原来: [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
// 修改为: [event]: [...(prev[event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
```

第 395 行:
```typescript
// 原来: [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
// 修改为: [event]: [...(prev[event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]), newCommand]
```

第 395 行:
```typescript
// 原来: [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
// 修改为: [event]: [...(prev[event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]), newCommand]
```

第 404 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
```

第 404 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).map(matcher =>
```

第 415 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
// 修改为: [event]: (prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
```

第 415 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
// 修改为: [event]: (prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
```

第 424 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
// 修改为: [event]: (prev[event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
```

第 424 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
// 修改为: [event]: (prev[event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
```

第 424 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
// 修改为: [event]: (prev[event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]).map(cmd =>
```

第 435 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
// 修改为: [event]: (prev[event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
```

第 435 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
// 修改为: [event]: (prev[event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
```

第 435 行:
```typescript
// 原来: [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
// 修改为: [event]: (prev[event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
```

第 455 行:
```typescript
// 原来: [template.event]: [...(prev[template.event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
// 修改为: [template.event]: [...(prev[template.event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
```

第 455 行:
```typescript
// 原来: [template.event]: [...(prev[template.event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
// 修改为: [template.event]: [...(prev[template.event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]), newMatcher]
```

第 467 行:
```typescript
// 原来: [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
// 修改为: [template.event]: [...(prev[template.event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
```

第 467 行:
```typescript
// 原来: [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
// 修改为: [template.event]: [...(prev[template.event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
```

第 467 行:
```typescript
// 原来: [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
// 修改为: [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]), ...newCommands]
```

第 502 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
```

第 502 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).map(matcher =>
```

第 520 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
```

第 520 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).map(matcher =>
```

第 538 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
```

第 538 行:
```typescript
// 原来: [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
// 修改为: [event]: (prev[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).map(matcher =>
```

第 560 行:
```typescript
// 原来: <Label htmlFor={`matcher-${matcher.id}`}>Pattern</Label>
// 修改为: <Label htmlFor={`matcher-${matcher.id}`}>Pattern</Label>
```

第 596 行:
```typescript
// 原来: <SelectItem value="custom">Custom</SelectItem>
// 修改为: <SelectItem value="custom">Custom</SelectItem>
```

第 626 行:
```typescript
// 原来: <Label>Commands</Label>
// 修改为: <Label>Commands</Label>
```

第 858 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {([t("category.pretooluse"), 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 858 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', t("category.posttooluse"), 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 858 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', t("category.notification"), 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 858 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', 'Notification', t("category.stop"), 'SubagentStop'] as HookEvent[]).map(event => {
```

第 858 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', t("category.subagentstop")] as HookEvent[]).map(event => {
```

第 861 行:
```typescript
// 原来: ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).length
// 修改为: ? (editableHooks[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[]).length
```

第 861 行:
```typescript
// 原来: ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).length
// 修改为: ? (editableHooks[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[]).length
```

第 862 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
// 修改为: : (editableHooks[event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
```

第 862 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
// 修改为: : (editableHooks[event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]).length;
```

第 862 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
// 修改为: : (editableHooks[event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]).length;
```

第 878 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {([t("category.pretooluse"), 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 878 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', t("category.posttooluse"), 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 878 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', t("category.notification"), 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
```

第 878 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', 'Notification', t("category.stop"), 'SubagentStop'] as HookEvent[]).map(event => {
```

第 878 行:
```typescript
// 原来: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
// 修改为: {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', t("category.subagentstop")] as HookEvent[]).map(event => {
```

第 881 行:
```typescript
// 原来: ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[])
// 修改为: ? (editableHooks[event as t("category.pretooluse") | 'PostToolUse'] as EditableHookMatcher[])
```

第 881 行:
```typescript
// 原来: ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[])
// 修改为: ? (editableHooks[event as 'PreToolUse' | t("category.posttooluse")] as EditableHookMatcher[])
```

第 882 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
// 修改为: : (editableHooks[event as t("category.notification") | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
```

第 882 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
// 修改为: : (editableHooks[event as 'Notification' | t("category.stop") | 'SubagentStop'] as EditableHookCommand[]);
```

第 882 行:
```typescript
// 原来: : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
// 修改为: : (editableHooks[event as 'Notification' | 'Stop' | t("category.subagentstop")] as EditableHookCommand[]);
```

## src/components/FilePicker.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 193 行:
```typescript
// 原来: case 'Escape':
// 修改为: case t("category.escape"):
```

第 198 行:
```typescript
// 原来: case 'Enter':
// 修改为: case t("category.enter"):
```

第 206 行:
```typescript
// 原来: case 'ArrowUp':
// 修改为: case t("category.arrowup"):
```

第 211 行:
```typescript
// 原来: case 'ArrowDown':
// 修改为: case t("category.arrowdown"):
```

第 216 行:
```typescript
// 原来: case 'ArrowRight':
// 修改为: case t("category.arrowright"):
```

第 227 行:
```typescript
// 原来: case 'ArrowLeft':
// 修改为: case t("category.arrowleft"):
```

第 453 行:
```typescript
// 原来: title={entry.is_directory ? "Click to select • Double-click to enter" : "Click to select"}
// 修改为: title={entry.is_directory ? "Click to select • Double-click to enter" : t("category.clickToSelect")}
```

## src/components/UsageDashboard.original.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 142 行:
```typescript
// 原来: {range === "all" ? "All Time" : range === "7d" ? "Last 7 Days" : "Last 30 Days"}
// 修改为: {range === "all" ? t("category.allTime") : range === "7d" ? "Last 7 Days" : "Last 30 Days"}
```

第 410 行:
```typescript
// 原来: <span>Daily Usage</span>
// 修改为: <span>Daily Usage</span>
```

## src/components/MCPAddServer.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 301 行:
```typescript
// 原来: <Label htmlFor="stdio-name">Server Name</Label>
// 修改为: <Label htmlFor="stdio-name">Server Name</Label>
```

第 314 行:
```typescript
// 原来: <Label htmlFor="stdio-command">Command</Label>
// 修改为: <Label htmlFor="stdio-command">Command</Label>
```

第 342 行:
```typescript
// 原来: <Label htmlFor="stdio-scope">Scope</Label>
// 修改为: <Label htmlFor="stdio-scope">Scope</Label>
```

第 384 行:
```typescript
// 原来: <Label htmlFor="sse-name">Server Name</Label>
// 修改为: <Label htmlFor="sse-name">Server Name</Label>
```

第 411 行:
```typescript
// 原来: <Label htmlFor="sse-scope">Scope</Label>
// 修改为: <Label htmlFor="sse-scope">Scope</Label>
```

第 454 行:
```typescript
// 原来: <span>Example Commands</span>
// 修改为: <span>Example Commands</span>
```

## src/components/CCAgents.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 198 行:
```typescript
// 原来: name: 'Claudia Agent',
// 修改为: name: t("category.claudiaAgent"),
```

第 227 行:
```typescript
// 原来: name: 'Claudia Agent',
// 修改为: name: t("category.claudiaAgent"),
```

## src/components/SessionOutputViewer.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 413 行:
```typescript
// 原来: title="Fullscreen"
// 修改为: title=t("category.fullscreen")
```

第 460 行:
```typescript
// 原来: title="Refresh output"
// 修改为: title=t("category.refreshOutput")
```

## src/components/IconPicker.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 267 行:
```typescript
// 原来: "Communication": [
// 修改为: t("category.communication"): [
```

第 277 行:
```typescript
// 原来: "Miscellaneous": [
// 修改为: t("category.miscellaneous"): [
```

第 371 行:
```typescript
// 原来: <DialogTitle>Choose an icon</DialogTitle>
// 修改为: <DialogTitle>Choose an icon</DialogTitle>
```

## src/components/SlashCommandsManager.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 53 行:
```typescript
// 原来: description: "Review code for best practices",
// 修改为: description: t("category.reviewCodeForBestPractices"),
```

第 55 行:
```typescript
// 原来: allowedTools: ["Read", "Grep"]
// 修改为: allowedTools: [t("category.read"), "Grep"]
```

第 55 行:
```typescript
// 原来: allowedTools: ["Read", "Grep"]
// 修改为: allowedTools: ["Read", t("category.grep")]
```

第 59 行:
```typescript
// 原来: description: "Explain how something works",
// 修改为: description: t("category.explainHowSomethingWorks"),
```

第 61 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: [t("category.read"), "Grep", "WebSearch"]
```

第 61 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: ["Read", t("category.grep"), "WebSearch"]
```

第 61 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: ["Read", "Grep", t("category.websearch")]
```

第 65 行:
```typescript
// 原来: description: "Fix a specific issue",
// 修改为: description: t("category.fixASpecificIssue"),
```

第 67 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: [t("category.read"), "Edit", "MultiEdit", "Write"]
```

第 67 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", t("category.edit"), "MultiEdit", "Write"]
```

第 67 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", "Edit", t("category.multiedit"), "Write"]
```

第 67 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", "Edit", "MultiEdit", t("category.write")]
```

第 71 行:
```typescript
// 原来: description: "Write tests for code",
// 修改为: description: t("category.writeTestsForCode"),
```

第 73 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: [t("category.read"), "Write", "Edit"]
```

第 73 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: ["Read", t("category.write"), "Edit"]
```

第 73 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: ["Read", "Write", t("category.edit")]
```

第 111 行:
```typescript
// 原来: allowedTools: ["Read", "Grep"]
// 修改为: allowedTools: [t("category.read"), "Grep"]
```

第 111 行:
```typescript
// 原来: allowedTools: ["Read", "Grep"]
// 修改为: allowedTools: ["Read", t("category.grep")]
```

第 117 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: [t("category.read"), "Grep", "WebSearch"]
```

第 117 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: ["Read", t("category.grep"), "WebSearch"]
```

第 117 行:
```typescript
// 原来: allowedTools: ["Read", "Grep", "WebSearch"]
// 修改为: allowedTools: ["Read", "Grep", t("category.websearch")]
```

第 123 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: [t("category.read"), "Edit", "MultiEdit", "Write"]
```

第 123 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", t("category.edit"), "MultiEdit", "Write"]
```

第 123 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", "Edit", t("category.multiedit"), "Write"]
```

第 123 行:
```typescript
// 原来: allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
// 修改为: allowedTools: ["Read", "Edit", "MultiEdit", t("category.write")]
```

第 129 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: [t("category.read"), "Write", "Edit"]
```

第 129 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: ["Read", t("category.write"), "Edit"]
```

第 129 行:
```typescript
// 原来: allowedTools: ["Read", "Write", "Edit"]
// 修改为: allowedTools: ["Read", "Write", t("category.edit")]
```

第 674 行:
```typescript
// 原来: <Label>Preview</Label>
// 修改为: <Label>Preview</Label>
```

## src/components/Settings.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 423 行:
```typescript
// 原来: <Label>Theme</Label>
// 修改为: <Label>Theme</Label>
```

第 625 行:
```typescript
// 原来: <Label htmlFor="verbose">Verbose Output</Label>
// 修改为: <Label htmlFor="verbose">Verbose Output</Label>
```

第 682 行:
```typescript
// 原来: <Label htmlFor="analytics-enabled">Enable Analytics</Label>
// 修改为: <Label htmlFor="analytics-enabled">Enable Analytics</Label>
```

第 728 行:
```typescript
// 原来: <Label htmlFor="tab-persistence">Remember Open Tabs</Label>
// 修改为: <Label htmlFor="tab-persistence">Remember Open Tabs</Label>
```

第 753 行:
```typescript
// 原来: <Label htmlFor="startup-intro">Show Welcome Intro on Startup</Label>
// 修改为: <Label htmlFor="startup-intro">Show Welcome Intro on Startup</Label>
```

第 768 行:
```typescript
// 原来: ? 'Welcome intro enabled'
// 修改为: ? t("category.welcomeIntroEnabled")
```

第 769 行:
```typescript
// 原来: : 'Welcome intro disabled',
// 修改为: : t("category.welcomeIntroDisabled"),
```

第 993 行:
```typescript
// 原来: <Label htmlFor="apiKeyHelper">API Key Helper Script</Label>
// 修改为: <Label htmlFor="apiKeyHelper">API Key Helper Script</Label>
```

## src/components/MCPImportExport.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 333 行:
```typescript
// 原来: <span>JSON Format Examples</span>
// 修改为: <span>JSON Format Examples</span>
```

## src/components/GitHubAgentBrowser.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 293 行:
```typescript
// 原来: <DialogTitle>Agent Preview</DialogTitle>
// 修改为: <DialogTitle>Agent Preview</DialogTitle>
```

## src/components/StreamMessage.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 473 行:
```typescript
// 原来: contentText.includes("MultiEdit completed successfully") ||
// 修改为: contentText.includes(t("category.multieditCompletedSuccessfully")) ||
```

第 474 行:
```typescript
// 原来: contentText.includes("Applied multiple edits to");
// 修改为: contentText.includes(t("category.appliedMultipleEditsTo"));
```

第 731 行:
```typescript
// 原来: {error instanceof Error ? error.message : 'Unknown error'}
// 修改为: {error instanceof Error ? error.message : t("category.unknownError")}
```

## src/lib/outputCache.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 106 行:
```typescript
// 原来: error: 'Failed to parse message',
// 修改为: error: t("category.failedToParseMessage"),
```

## src/contexts/TabContext.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 86 行:
```typescript
// 原来: title: 'Projects',
// 修改为: title: t("category.projects"),
```

## src/components/claude-code-session/MessageList.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 84 行:
```typescript
// 原来: ? "Enter a prompt below to begin your Claude Code session"
// 修改为: ? t("category.enterAPromptBelowToBeginYourClaudeCodeSession")
```

第 85 行:
```typescript
// 原来: : "Select a project folder to begin"}
// 修改为: : t("category.selectAProjectFolderToBegin")}
```

## src/components/claude-code-session/PromptQueue.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 65 行:
```typescript
// 原来: {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
// 修改为: {queuedPrompt.model === "opus" ? t("category.opus") : "Sonnet"}
```

第 65 行:
```typescript
// 原来: {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
// 修改为: {queuedPrompt.model === "opus" ? "Opus" : t("category.sonnet")}
```

## src/components/widgets/BashWidget.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 65 行:
```typescript
// 原来: {resultContent || (isError ? "Command failed" : "Command completed")}
// 修改为: {resultContent || (isError ? t("category.commandFailed") : "Command completed")}
```

第 65 行:
```typescript
// 原来: {resultContent || (isError ? "Command failed" : "Command completed")}
// 修改为: {resultContent || (isError ? "Command failed" : t("category.commandCompleted"))}
```

## src/components/ui/split-pane.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 133 行:
```typescript
// 原来: case 'ArrowLeft':
// 修改为: case t("category.arrowleft"):
```

第 137 行:
```typescript
// 原来: case 'ArrowRight':
// 修改为: case t("category.arrowright"):
```

第 141 行:
```typescript
// 原来: case 'Home':
// 修改为: case t("category.home"):
```

## src/components/ui/scroll-area.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 37 行:
```typescript
// 原来: ScrollArea.displayName = "ScrollArea";
// 修改为: ScrollArea.displayName = t("category.scrollarea");
```

## src/components/ui/label.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 26 行:
```typescript
// 原来: Label.displayName = "Label";
// 修改为: Label.displayName = t("category.label");
```

## src/components/ui/dropdown-menu.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 180 行:
```typescript
// 原来: DropdownMenuShortcut.displayName = "DropdownMenuShortcut"
// 修改为: DropdownMenuShortcut.displayName = t("category.dropdownmenushortcut")
```

## src/components/ui/tabs.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 80 行:
```typescript
// 原来: TabsList.displayName = "TabsList";
// 修改为: TabsList.displayName = t("category.tabslist");
```

第 122 行:
```typescript
// 原来: TabsTrigger.displayName = "TabsTrigger";
// 修改为: TabsTrigger.displayName = t("category.tabstrigger");
```

第 155 行:
```typescript
// 原来: TabsContent.displayName = "TabsContent";
// 修改为: TabsContent.displayName = t("category.tabscontent");
```

## src/components/ui/button.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 63 行:
```typescript
// 原来: Button.displayName = "Button";
// 修改为: Button.displayName = t("category.button");
```

## src/components/ui/switch.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 63 行:
```typescript
// 原来: Switch.displayName = "Switch";
// 修改为: Switch.displayName = t("category.switch");
```

## src/components/ui/card.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 39 行:
```typescript
// 原来: Card.displayName = "Card";
// 修改为: Card.displayName = t("category.card");
```

第 54 行:
```typescript
// 原来: CardHeader.displayName = "CardHeader";
// 修改为: CardHeader.displayName = t("category.cardheader");
```

第 69 行:
```typescript
// 原来: CardTitle.displayName = "CardTitle";
// 修改为: CardTitle.displayName = t("category.cardtitle");
```

第 84 行:
```typescript
// 原来: CardDescription.displayName = "CardDescription";
// 修改为: CardDescription.displayName = t("category.carddescription");
```

第 95 行:
```typescript
// 原来: CardContent.displayName = "CardContent";
// 修改为: CardContent.displayName = t("category.cardcontent");
```

第 110 行:
```typescript
// 原来: CardFooter.displayName = "CardFooter";
// 修改为: CardFooter.displayName = t("category.cardfooter");
```

## src/components/ui/input.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 37 行:
```typescript
// 原来: Input.displayName = "Input";
// 修改为: Input.displayName = t("category.input");
```

## src/components/ui/select.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 194 行:
```typescript
// 原来: placeholder = "Select an option",
// 修改为: placeholder = t("category.selectAnOption"),
```

## src/components/ui/dialog.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 65 行:
```typescript
// 原来: DialogHeader.displayName = "DialogHeader"
// 修改为: DialogHeader.displayName = t("category.dialogheader")
```

第 79 行:
```typescript
// 原来: DialogFooter.displayName = "DialogFooter"
// 修改为: DialogFooter.displayName = t("category.dialogfooter")
```

## src/components/ui/textarea.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 21 行:
```typescript
// 原来: Textarea.displayName = "Textarea"
// 修改为: Textarea.displayName = t("category.textarea")
```

## src/components/ui/popover.tsx

需要添加以下导入:
```typescript
import { useI18n } from '@/lib/i18n';
```

在组件中添加:
```typescript
const { t } = useI18n();
```

替换以下文本:
第 86 行:
```typescript
// 原来: if (event.key === "Escape") {
// 修改为: if (event.key === t("category.escape")) {
```
