# Claudia 项目硬编码英文文本检查报告

扫描时间: 2025-08-22 19:24:37

总计发现 334 个硬编码英文文本，分布在 60 个文件中。

## 按文件分组

### src/components/AgentExecution.tsx (2 个文本)

- **第 107 行**: `AgentExecution`
  ```typescript
  useComponentMetrics('AgentExecution');
  ```

- **第 713 行**: `Enter`
  ```typescript
  if (e.key === "Enter" && !isRunning && projectPath && task.trim()) {
  ```

### src/components/AgentExecutionDemo.tsx (4 个文本)

- **第 22 行**: `JSONL Viewer Model Configuration and Setup`
  ```typescript
  summary: "JSONL Viewer Model Configuration and Setup",
  ```

- **第 32 行**: `Edit`
  ```typescript
  name: "Edit",
  ```

- **第 93 行**: `Write`
  ```typescript
  name: "Write",
  ```

- **第 104 行**: `Segoe UI`
  ```typescript
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  ```

### src/components/AgentRunOutputViewer.tsx (8 个文本)

- **第 109 行**: `Unknown`
  ```typescript
  updateTabTitle(tabId, `Agent: ${agentRun.agent_name || 'Unknown'}`);
  ```

- **第 417 行**: `Execution stopped by user`
  ```typescript
  result: "Execution stopped by user",
  ```

- **第 438 行**: `Unknown error`
  ```typescript
  message: `Failed to stop execution: ${err instanceof Error ? err.message : 'Unknown error'}`,
  ```

- **第 634 行**: `Exit fullscreen`
  ```typescript
  title={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
  ```

- **第 634 行**: `Enter fullscreen`
  ```typescript
  title={isFullscreen ? "Exit fullscreen" : "Enter fullscreen"}
  ```

- **第 648 行**: `Refresh output`
  ```typescript
  title="Refresh output"
  ```

- **第 659 行**: `Stop execution`
  ```typescript
  title="Stop execution"
  ```

- **第 678 行**: `No output available yet`
  ```typescript
  <p>No output available yet</p>
  ```

### src/components/AgentRunView.tsx (1 个文本)

- **第 239 行**: `Go Back`
  ```typescript
  <Button onClick={onBack}>Go Back</Button>
  ```

### src/components/AgentRunsList.tsx (4 个文本)

- **第 174 行**: `Completed`
  ```typescript
  {run.status === "completed" ? "Completed" :
  ```

- **第 175 行**: `Running`
  ```typescript
  run.status === "running" ? "Running" :
  ```

- **第 176 行**: `Failed`
  ```typescript
  run.status === "failed" ? "Failed" :
  ```

- **第 177 行**: `Pending`
  ```typescript
  "Pending"}
  ```

### src/components/Agents.tsx (3 个文本)

- **第 125 行**: `JSON Files`
  ```typescript
  { name: 'JSON Files', extensions: ['json'] },
  ```

- **第 126 行**: `All Files`
  ```typescript
  { name: 'All Files', extensions: ['*'] }
  ```

- **第 150 行**: `JSON Files`
  ```typescript
  { name: 'JSON Files', extensions: ['json'] }
  ```

### src/components/AgentsModal.tsx (2 个文本)

- **第 232 行**: `Available Agents`
  ```typescript
  <TabsTrigger value="agents">Available Agents</TabsTrigger>
  ```

- **第 412 行**: `Delete Agent`
  ```typescript
  <DialogTitle>Delete Agent</DialogTitle>
  ```

### src/components/AnalyticsErrorBoundary.tsx (1 个文本)

- **第 31 行**: `UnknownError`
  ```typescript
  error_type: error.name || 'UnknownError',
  ```

### src/components/CCAgents.tsx (2 个文本)

- **第 198 行**: `Claudia Agent`
  ```typescript
  name: 'Claudia Agent',
  ```

- **第 227 行**: `Claudia Agent`
  ```typescript
  name: 'Claudia Agent',
  ```

### src/components/ClaudeBinaryDialog.tsx (1 个文本)

- **第 55 行**: `Failed to save Claude binary path`
  ```typescript
  onError(error instanceof Error ? error.message : "Failed to save Claude binary path");
  ```

### src/components/ClaudeCodeSession.refactored.tsx (5 个文本)

- **第 98 行**: `Select Project Directory`
  ```typescript
  title: "Select Project Directory"
  ```

- **第 130 行**: `Failed to send prompt`
  ```typescript
  setError(error instanceof Error ? error.message : "Failed to send prompt");
  ```

- **第 368 行**: `Fork Session from Checkpoint`
  ```typescript
  <DialogTitle>Fork Session from Checkpoint</DialogTitle>
  ```

- **第 375 行**: `New Session Name`
  ```typescript
  <Label htmlFor="fork-name">New Session Name</Label>
  ```

- **第 380 行**: `Enter a name for the forked session`
  ```typescript
  placeholder="Enter a name for the forked session"
  ```

### src/components/ClaudeCodeSession.tsx (22 个文本)

- **第 138 行**: `ClaudeCodeSession`
  ```typescript
  useComponentMetrics('ClaudeCodeSession');
  ```

- **第 334 行**: `Failed to load session history`
  ```typescript
  setError("Failed to load session history");
  ```

- **第 346 行**: `ClaudeSession`
  ```typescript
  if ('process_type' in s && s.process_type && 'ClaudeSession' in s.process_type) {
  ```

- **第 437 行**: `Please select a project directory first`
  ```typescript
  setError("Please select a project directory first");
  ```

- **第 595 行**: `Tool execution failed`
  ```typescript
  context: `Tool execution failed`,
  ```

- **第 817 行**: `Failed to send prompt`
  ```typescript
  setError("Failed to send prompt");
  ```

- **第 994 行**: `Session cancelled by user`
  ```typescript
  result: "Session cancelled by user",
  ```

- **第 1006 行**: `Unknown error`
  ```typescript
  result: `Failed to cancel execution: ${err instanceof Error ? err.message : 'Unknown error'}. The process may still be running in the background.`,
  ```

- **第 1055 行**: `Failed to fork checkpoint`
  ```typescript
  setError("Failed to fork checkpoint");
  ```

- **第 1306 行**: `Expand queue`
  ```typescript
  <TooltipSimple content={queuedPromptsCollapsed ? "Expand queue" : "Collapse queue"} side="top">
  ```

- **第 1306 行**: `Collapse queue`
  ```typescript
  <TooltipSimple content={queuedPromptsCollapsed ? "Expand queue" : "Collapse queue"} side="top">
  ```

- **第 1330 行**: `Opus`
  ```typescript
  {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
  ```

- **第 1330 行**: `Sonnet`
  ```typescript
  {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
  ```

- **第 1365 行**: `Scroll to top`
  ```typescript
  <TooltipSimple content="Scroll to top" side="top">
  ```

- **第 1403 行**: `Scroll to bottom`
  ```typescript
  <TooltipSimple content="Scroll to bottom" side="top">
  ```

- **第 1448 行**: `Session Timeline`
  ```typescript
  <TooltipSimple content="Session Timeline" side="top">
  ```

- **第 1467 行**: `Copy conversation`
  ```typescript
  <TooltipSimple content="Copy conversation" side="top">
  ```

- **第 1508 行**: `Checkpoint Settings`
  ```typescript
  <TooltipSimple content="Checkpoint Settings" side="top">
  ```

- **第 1598 行**: `Fork Session`
  ```typescript
  <DialogTitle>Fork Session</DialogTitle>
  ```

- **第 1606 行**: `New Session Name`
  ```typescript
  <Label htmlFor="fork-name">New Session Name</Label>
  ```

- **第 1613 行**: `Enter`
  ```typescript
  if (e.key === "Enter" && !isLoading) {
  ```

- **第 1658 行**: `Slash Commands`
  ```typescript
  <DialogTitle>Slash Commands</DialogTitle>
  ```

### src/components/ClaudeVersionSelector.tsx (16 个文本)

- **第 100 行**: `Failed to load Claude installations`
  ```typescript
  setError(err instanceof Error ? err.message : "Failed to load Claude installations");
  ```

- **第 116 行**: `System`
  ```typescript
  case "System":
  ```

- **第 118 行**: `Custom`
  ```typescript
  case "Custom":
  ```

- **第 127 行**: `System`
  ```typescript
  case "System":
  ```

- **第 129 行**: `Custom`
  ```typescript
  case "Custom":
  ```

- **第 150 行**: `Claude Code Installation`
  ```typescript
  <CardTitle>Claude Code Installation</CardTitle>
  ```

- **第 179 行**: `Claude Code Installation`
  ```typescript
  <CardTitle>Claude Code Installation</CardTitle>
  ```

- **第 180 行**: `Error loading installations`
  ```typescript
  <CardDescription>Error loading installations</CardDescription>
  ```

- **第 192 行**: `System`
  ```typescript
  const systemInstallations = installations.filter(i => i.installation_type === "System");
  ```

- **第 193 行**: `Custom`
  ```typescript
  const customInstallations = installations.filter(i => i.installation_type === "Custom");
  ```

- **第 215 行**: `Choose Claude installation`
  ```typescript
  <SelectValue placeholder="Choose Claude installation">
  ```

- **第 241 行**: `Unknown version`
  ```typescript
  <span>{installation.version || "Unknown version"}</span>
  ```

- **第 287 行**: `Select Claude installation`
  ```typescript
  <SelectValue placeholder="Select Claude installation">
  ```

- **第 310 行**: `Version unknown`
  ```typescript
  {installation.version || "Version unknown"} • {installation.source}
  ```

- **第 332 行**: `Version unknown`
  ```typescript
  {installation.version || "Version unknown"} • {installation.source}
  ```

- **第 373 行**: `Save Selection`
  ```typescript
  {isSaving ? "Saving..." : "Save Selection"}
  ```

### src/components/CreateAgent.tsx (1 个文本)

- **第 141 行**: `Back to Agents`
  ```typescript
  title="Back to Agents"
  ```

### src/components/FilePicker.optimized.tsx (9 个文本)

- **第 140 行**: `Failed to load directory`
  ```typescript
  setError(err instanceof Error ? err.message : 'Failed to load directory');
  ```

- **第 168 行**: `Search failed`
  ```typescript
  setError(err instanceof Error ? err.message : 'Search failed');
  ```

- **第 197 行**: `ArrowUp`
  ```typescript
  case 'ArrowUp':
  ```

- **第 201 行**: `ArrowDown`
  ```typescript
  case 'ArrowDown':
  ```

- **第 205 行**: `Enter`
  ```typescript
  case 'Enter':
  ```

- **第 216 行**: `Escape`
  ```typescript
  case 'Escape':
  ```

- **第 335 行**: `No files found`
  ```typescript
  {searchQuery.trim() ? 'No files found' : 'Empty directory'}
  ```

- **第 335 行**: `Empty directory`
  ```typescript
  {searchQuery.trim() ? 'No files found' : 'Empty directory'}
  ```

- **第 375 行**: `Click to select`
  ```typescript
  title={entry.is_directory ? "Click to select • Double-click to enter" : "Click to select"}
  ```

### src/components/FilePicker.tsx (7 个文本)

- **第 193 行**: `Escape`
  ```typescript
  case 'Escape':
  ```

- **第 198 行**: `Enter`
  ```typescript
  case 'Enter':
  ```

- **第 206 行**: `ArrowUp`
  ```typescript
  case 'ArrowUp':
  ```

- **第 211 行**: `ArrowDown`
  ```typescript
  case 'ArrowDown':
  ```

- **第 216 行**: `ArrowRight`
  ```typescript
  case 'ArrowRight':
  ```

- **第 227 行**: `ArrowLeft`
  ```typescript
  case 'ArrowLeft':
  ```

- **第 453 行**: `Click to select`
  ```typescript
  title={entry.is_directory ? "Click to select • Double-click to enter" : "Click to select"}
  ```

### src/components/FloatingPromptInput.tsx (10 个文本)

- **第 189 行**: `Deeper analysis`
  ```typescript
  description: "Deeper analysis",
  ```

- **第 198 行**: `Think Harder`
  ```typescript
  name: "Think Harder",
  ```

- **第 199 行**: `Extensive reasoning`
  ```typescript
  description: "Extensive reasoning",
  ```

- **第 654 行**: `Escape`
  ```typescript
  if (showFilePicker && e.key === 'Escape') {
  ```

- **第 661 行**: `Escape`
  ```typescript
  if (showSlashCommandPicker && e.key === 'Escape') {
  ```

- **第 675 行**: `Enter`
  ```typescript
  if (e.key === "Enter" && !e.shiftKey && !isExpanded && !showFilePicker && !showSlashCommandPicker) {
  ```

- **第 800 行**: `Minimize`
  ```typescript
  <TooltipSimple content="Minimize" side="bottom">
  ```

- **第 960 行**: `Send message`
  ```typescript
  <TooltipSimple content="Send message" side="top">
  ```

- **第 1186 行**: `Stop generation`
  ```typescript
  <TooltipSimple content={isLoading ? "Stop generation" : "Send message (Enter)"} side="top">
  ```

- **第 1256 行**: `FloatingPromptInput`
  ```typescript
  FloatingPromptInput.displayName = 'FloatingPromptInput';
  ```

### src/components/GitHubAgentBrowser.tsx (1 个文本)

- **第 293 行**: `Agent Preview`
  ```typescript
  <DialogTitle>Agent Preview</DialogTitle>
  ```

### src/components/HooksEditor.tsx (63 个文本)

- **第 86 行**: `Pre Tool Use`
  ```typescript
  label: 'Pre Tool Use',
  ```

- **第 91 行**: `Post Tool Use`
  ```typescript
  label: 'Post Tool Use',
  ```

- **第 92 行**: `Runs after successful tool completion`
  ```typescript
  description: 'Runs after successful tool completion',
  ```

- **第 96 行**: `Notification`
  ```typescript
  label: 'Notification',
  ```

- **第 97 行**: `Customizes notifications when Claude needs attention`
  ```typescript
  description: 'Customizes notifications when Claude needs attention',
  ```

- **第 101 行**: `Stop`
  ```typescript
  label: 'Stop',
  ```

- **第 102 行**: `Runs when Claude finishes responding`
  ```typescript
  description: 'Runs when Claude finishes responding',
  ```

- **第 106 行**: `Subagent Stop`
  ```typescript
  label: 'Subagent Stop',
  ```

- **第 153 行**: `PreToolUse`
  ```typescript
  const [selectedEvent, setSelectedEvent] = useState<HookEvent>('PreToolUse');
  ```

- **第 165 行**: `PreToolUse`
  ```typescript
  const matcherEvents = ['PreToolUse', 'PostToolUse'] as const;
  ```

- **第 165 行**: `PostToolUse`
  ```typescript
  const matcherEvents = ['PreToolUse', 'PostToolUse'] as const;
  ```

- **第 167 行**: `Notification`
  ```typescript
  const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
  ```

- **第 167 行**: `Stop`
  ```typescript
  const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
  ```

- **第 167 行**: `SubagentStop`
  ```typescript
  const directEvents = ['Notification', 'Stop', 'SubagentStop'] as const;
  ```

- **第 379 行**: `PreToolUse`
  ```typescript
  [event]: [...(prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
  ```

- **第 379 行**: `PostToolUse`
  ```typescript
  [event]: [...(prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
  ```

- **第 395 行**: `Notification`
  ```typescript
  [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
  ```

- **第 395 行**: `Stop`
  ```typescript
  [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
  ```

- **第 395 行**: `SubagentStop`
  ```typescript
  [event]: [...(prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), newCommand]
  ```

- **第 404 行**: `PreToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 404 行**: `PostToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 415 行**: `PreToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
  ```

- **第 415 行**: `PostToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).filter(matcher => matcher.id !== matcherId)
  ```

- **第 424 行**: `Notification`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
  ```

- **第 424 行**: `Stop`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
  ```

- **第 424 行**: `SubagentStop`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).map(cmd =>
  ```

- **第 435 行**: `Notification`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
  ```

- **第 435 行**: `Stop`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
  ```

- **第 435 行**: `SubagentStop`
  ```typescript
  [event]: (prev[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).filter(cmd => cmd.id !== commandId)
  ```

- **第 455 行**: `PreToolUse`
  ```typescript
  [template.event]: [...(prev[template.event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
  ```

- **第 455 行**: `PostToolUse`
  ```typescript
  [template.event]: [...(prev[template.event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]), newMatcher]
  ```

- **第 467 行**: `Notification`
  ```typescript
  [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
  ```

- **第 467 行**: `Stop`
  ```typescript
  [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
  ```

- **第 467 行**: `SubagentStop`
  ```typescript
  [template.event]: [...(prev[template.event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]), ...newCommands]
  ```

- **第 502 行**: `PreToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 502 行**: `PostToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 520 行**: `PreToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 520 行**: `PostToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 538 行**: `PreToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 538 行**: `PostToolUse`
  ```typescript
  [event]: (prev[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).map(matcher =>
  ```

- **第 560 行**: `Pattern`
  ```typescript
  <Label htmlFor={`matcher-${matcher.id}`}>Pattern</Label>
  ```

- **第 596 行**: `Custom`
  ```typescript
  <SelectItem value="custom">Custom</SelectItem>
  ```

- **第 626 行**: `Commands`
  ```typescript
  <Label>Commands</Label>
  ```

- **第 858 行**: `PreToolUse`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 858 行**: `PostToolUse`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 858 行**: `Notification`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 858 行**: `Stop`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 858 行**: `SubagentStop`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 861 行**: `PreToolUse`
  ```typescript
  ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).length
  ```

- **第 861 行**: `PostToolUse`
  ```typescript
  ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[]).length
  ```

- **第 862 行**: `Notification`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
  ```

- **第 862 行**: `Stop`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
  ```

- **第 862 行**: `SubagentStop`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]).length;
  ```

- **第 878 行**: `PreToolUse`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 878 行**: `PostToolUse`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 878 行**: `Notification`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 878 行**: `Stop`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 878 行**: `SubagentStop`
  ```typescript
  {(['PreToolUse', 'PostToolUse', 'Notification', 'Stop', 'SubagentStop'] as HookEvent[]).map(event => {
  ```

- **第 881 行**: `PreToolUse`
  ```typescript
  ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[])
  ```

- **第 881 行**: `PostToolUse`
  ```typescript
  ? (editableHooks[event as 'PreToolUse' | 'PostToolUse'] as EditableHookMatcher[])
  ```

- **第 882 行**: `Notification`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
  ```

- **第 882 行**: `Stop`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
  ```

- **第 882 行**: `SubagentStop`
  ```typescript
  : (editableHooks[event as 'Notification' | 'Stop' | 'SubagentStop'] as EditableHookCommand[]);
  ```

### src/components/IconPicker.tsx (3 个文本)

- **第 267 行**: `Communication`
  ```typescript
  "Communication": [
  ```

- **第 277 行**: `Miscellaneous`
  ```typescript
  "Miscellaneous": [
  ```

- **第 371 行**: `Choose an icon`
  ```typescript
  <DialogTitle>Choose an icon</DialogTitle>
  ```

### src/components/MCPAddServer.tsx (6 个文本)

- **第 301 行**: `Server Name`
  ```typescript
  <Label htmlFor="stdio-name">Server Name</Label>
  ```

- **第 314 行**: `Command`
  ```typescript
  <Label htmlFor="stdio-command">Command</Label>
  ```

- **第 342 行**: `Scope`
  ```typescript
  <Label htmlFor="stdio-scope">Scope</Label>
  ```

- **第 384 行**: `Server Name`
  ```typescript
  <Label htmlFor="sse-name">Server Name</Label>
  ```

- **第 411 行**: `Scope`
  ```typescript
  <Label htmlFor="sse-scope">Scope</Label>
  ```

- **第 454 行**: `Example Commands`
  ```typescript
  <span>Example Commands</span>
  ```

### src/components/MCPImportExport.tsx (1 个文本)

- **第 333 行**: `JSON Format Examples`
  ```typescript
  <span>JSON Format Examples</span>
  ```

### src/components/NFOCredits.tsx (16 个文本)

- **第 91 行**: `POWERED BY`
  ```typescript
  { type: "credit", role: "POWERED BY", name: "Anthropic Claude 4" },
  ```

- **第 92 行**: `CLAUDE CODE`
  ```typescript
  { type: "credit", role: "CLAUDE CODE", name: "The Ultimate Coding Assistant" },
  ```

- **第 92 行**: `The Ultimate Coding Assistant`
  ```typescript
  { type: "credit", role: "CLAUDE CODE", name: "The Ultimate Coding Assistant" },
  ```

- **第 93 行**: `MCP PROTOCOL`
  ```typescript
  { type: "credit", role: "MCP PROTOCOL", name: "Model Context Protocol" },
  ```

- **第 93 行**: `Model Context Protocol`
  ```typescript
  { type: "credit", role: "MCP PROTOCOL", name: "Model Context Protocol" },
  ```

- **第 96 行**: `Tauri Framework`
  ```typescript
  { type: "credit", role: "RUNTIME", name: "Tauri Framework" },
  ```

- **第 97 行**: `UI FRAMEWORK`
  ```typescript
  { type: "credit", role: "UI FRAMEWORK", name: "React + TypeScript" },
  ```

- **第 99 行**: `Framer Motion`
  ```typescript
  { type: "credit", role: "ANIMATIONS", name: "Framer Motion" },
  ```

- **第 100 行**: `BUILD TOOL`
  ```typescript
  { type: "credit", role: "BUILD TOOL", name: "Vite" },
  ```

- **第 100 行**: `Vite`
  ```typescript
  { type: "credit", role: "BUILD TOOL", name: "Vite" },
  ```

- **第 101 行**: `PACKAGE MANAGER`
  ```typescript
  { type: "credit", role: "PACKAGE MANAGER", name: "Bun" },
  ```

- **第 104 行**: `To the open source community`
  ```typescript
  { type: "text", content: "To the open source community" },
  ```

- **第 105 行**: `To all the beta testers`
  ```typescript
  { type: "text", content: "To all the beta testers" },
  ```

- **第 106 行**: `To everyone who believed in this project`
  ```typescript
  { type: "text", content: "To everyone who believed in this project" },
  ```

- **第 162 行**: `File a bug`
  ```typescript
  title="File a bug"
  ```

- **第 205 行**: `Asterisk`
  ```typescript
  alt="Asterisk"
  ```

### src/components/PreviewPromptDialog.tsx (2 个文本)

- **第 82 行**: `Local Development Server`
  ```typescript
  {isLocalhost ? 'Local Development Server' : 'External URL'}
  ```

- **第 82 行**: `External URL`
  ```typescript
  {isLocalhost ? 'Local Development Server' : 'External URL'}
  ```

### src/components/ProxySettings.tsx (6 个文本)

- **第 52 行**: `Failed to save proxy settings`
  ```typescript
  message: 'Failed to save proxy settings',
  ```

- **第 75 行**: `Failed to load proxy settings`
  ```typescript
  message: 'Failed to load proxy settings',
  ```

- **第 101 行**: `Enable Proxy`
  ```typescript
  <Label htmlFor="proxy-enabled">Enable Proxy</Label>
  ```

- **第 115 行**: `HTTP Proxy`
  ```typescript
  <Label htmlFor="http-proxy">HTTP Proxy</Label>
  ```

- **第 126 行**: `HTTPS Proxy`
  ```typescript
  <Label htmlFor="https-proxy">HTTPS Proxy</Label>
  ```

- **第 137 行**: `No Proxy`
  ```typescript
  <Label htmlFor="no-proxy">No Proxy</Label>
  ```

### src/components/RunningClaudeSessions.tsx (3 个文本)

- **第 47 行**: `Failed to load running sessions`
  ```typescript
  setError("Failed to load running sessions");
  ```

- **第 55 行**: `ClaudeSession`
  ```typescript
  if ('ClaudeSession' in processInfo.process_type) {
  ```

- **第 111 行**: `ClaudeSession`
  ```typescript
  const sessionId = 'ClaudeSession' in session.process_type
  ```

### src/components/SessionList.optimized.tsx (2 个文本)

- **第 30 行**: `Unknown time`
  ```typescript
  if (!timestamp) return "Unknown time";
  ```

- **第 102 行**: `SessionCard`
  ```typescript
  SessionCard.displayName = 'SessionCard';
  ```

### src/components/SessionOutputViewer.tsx (2 个文本)

- **第 413 行**: `Fullscreen`
  ```typescript
  title="Fullscreen"
  ```

- **第 460 行**: `Refresh output`
  ```typescript
  title="Refresh output"
  ```

### src/components/Settings.tsx (8 个文本)

- **第 423 行**: `Theme`
  ```typescript
  <Label>Theme</Label>
  ```

- **第 625 行**: `Verbose Output`
  ```typescript
  <Label htmlFor="verbose">Verbose Output</Label>
  ```

- **第 682 行**: `Enable Analytics`
  ```typescript
  <Label htmlFor="analytics-enabled">Enable Analytics</Label>
  ```

- **第 728 行**: `Remember Open Tabs`
  ```typescript
  <Label htmlFor="tab-persistence">Remember Open Tabs</Label>
  ```

- **第 753 行**: `Show Welcome Intro on Startup`
  ```typescript
  <Label htmlFor="startup-intro">Show Welcome Intro on Startup</Label>
  ```

- **第 768 行**: `Welcome intro enabled`
  ```typescript
  ? 'Welcome intro enabled'
  ```

- **第 769 行**: `Welcome intro disabled`
  ```typescript
  : 'Welcome intro disabled',
  ```

- **第 993 行**: `API Key Helper Script`
  ```typescript
  <Label htmlFor="apiKeyHelper">API Key Helper Script</Label>
  ```

### src/components/SlashCommandPicker.tsx (14 个文本)

- **第 170 行**: `Escape`
  ```typescript
  case 'Escape':
  ```

- **第 175 行**: `Enter`
  ```typescript
  case 'Enter':
  ```

- **第 188 行**: `ArrowUp`
  ```typescript
  case 'ArrowUp':
  ```

- **第 193 行**: `ArrowDown`
  ```typescript
  case 'ArrowDown':
  ```

- **第 224 行**: `Failed to load commands`
  ```typescript
  setError(err instanceof Error ? err.message : 'Failed to load commands');
  ```

- **第 244 行**: `User Commands`
  ```typescript
  key = cmd.namespace ? `User Commands: ${cmd.namespace}` : "User Commands";
  ```

- **第 246 行**: `Project Commands`
  ```typescript
  key = cmd.namespace ? `Project Commands: ${cmd.namespace}` : "Project Commands";
  ```

- **第 248 行**: `Commands`
  ```typescript
  key = cmd.namespace || "Commands";
  ```

- **第 302 行**: `Default`
  ```typescript
  <TabsTrigger value="default">Default</TabsTrigger>
  ```

- **第 303 行**: `Custom`
  ```typescript
  <TabsTrigger value="custom">Custom</TabsTrigger>
  ```

- **第 333 行**: `No commands found`
  ```typescript
  {searchQuery ? 'No commands found' : 'No default commands available'}
  ```

- **第 333 行**: `No default commands available`
  ```typescript
  {searchQuery ? 'No commands found' : 'No default commands available'}
  ```

- **第 395 行**: `No commands found`
  ```typescript
  {searchQuery ? 'No commands found' : 'No custom commands available'}
  ```

- **第 395 行**: `No custom commands available`
  ```typescript
  {searchQuery ? 'No commands found' : 'No custom commands available'}
  ```

### src/components/SlashCommandsManager.tsx (29 个文本)

- **第 53 行**: `Review code for best practices`
  ```typescript
  description: "Review code for best practices",
  ```

- **第 55 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Grep"]
  ```

- **第 55 行**: `Grep`
  ```typescript
  allowedTools: ["Read", "Grep"]
  ```

- **第 59 行**: `Explain how something works`
  ```typescript
  description: "Explain how something works",
  ```

- **第 61 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 61 行**: `Grep`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 61 行**: `WebSearch`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 65 行**: `Fix a specific issue`
  ```typescript
  description: "Fix a specific issue",
  ```

- **第 67 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 67 行**: `Edit`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 67 行**: `MultiEdit`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 67 行**: `Write`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 71 行**: `Write tests for code`
  ```typescript
  description: "Write tests for code",
  ```

- **第 73 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 73 行**: `Write`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 73 行**: `Edit`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 111 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Grep"]
  ```

- **第 111 行**: `Grep`
  ```typescript
  allowedTools: ["Read", "Grep"]
  ```

- **第 117 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 117 行**: `Grep`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 117 行**: `WebSearch`
  ```typescript
  allowedTools: ["Read", "Grep", "WebSearch"]
  ```

- **第 123 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 123 行**: `Edit`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 123 行**: `MultiEdit`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 123 行**: `Write`
  ```typescript
  allowedTools: ["Read", "Edit", "MultiEdit", "Write"]
  ```

- **第 129 行**: `Read`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 129 行**: `Write`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 129 行**: `Edit`
  ```typescript
  allowedTools: ["Read", "Write", "Edit"]
  ```

- **第 674 行**: `Preview`
  ```typescript
  <Label>Preview</Label>
  ```

### src/components/StartupIntro.tsx (1 个文本)

- **第 70 行**: `Claudia`
  ```typescript
  alt="Claudia"
  ```

### src/components/StorageTab.tsx (6 个文本)

- **第 578 行**: `Edit Row`
  ```typescript
  <DialogTitle>Edit Row</DialogTitle>
  ```

- **第 655 行**: `New Row`
  ```typescript
  <DialogTitle>New Row</DialogTitle>
  ```

- **第 729 行**: `Delete Row`
  ```typescript
  <DialogTitle>Delete Row</DialogTitle>
  ```

- **第 776 行**: `Reset Database`
  ```typescript
  <DialogTitle>Reset Database</DialogTitle>
  ```

- **第 816 行**: `SQL Query Editor`
  ```typescript
  <DialogTitle>SQL Query Editor</DialogTitle>
  ```

- **第 823 行**: `SQL Query`
  ```typescript
  <Label htmlFor="sql-query">SQL Query</Label>
  ```

### src/components/StreamMessage.tsx (3 个文本)

- **第 473 行**: `MultiEdit completed successfully`
  ```typescript
  contentText.includes("MultiEdit completed successfully") ||
  ```

- **第 474 行**: `Applied multiple edits to`
  ```typescript
  contentText.includes("Applied multiple edits to");
  ```

- **第 731 行**: `Unknown error`
  ```typescript
  {error instanceof Error ? error.message : 'Unknown error'}
  ```

### src/components/TabContent.tsx (6 个文本)

- **第 92 行**: `Select Project Folder`
  ```typescript
  title: 'Select Project Folder',
  ```

- **第 106 行**: `Failed to open folder picker`
  ```typescript
  setError('Failed to open folder picker');
  ```

- **第 124 行**: `New Session`
  ```typescript
  title: 'New Session',
  ```

- **第 159 行**: `Projects`
  ```typescript
  title: 'Projects'
  ```

- **第 163 行**: `Back to Projects`
  ```typescript
  title="Back to Projects"
  ```

- **第 258 行**: `Projects`
  ```typescript
  title: 'Projects',
  ```

### src/components/TabManager.tsx (4 个文本)

- **第 105 行**: `Unsaved changes`
  ```typescript
  title="Unsaved changes"
  ```

- **第 323 行**: `Scroll tabs left`
  ```typescript
  title="Scroll tabs left"
  ```

- **第 372 行**: `Maximum tabs reached`
  ```typescript
  title={canAddTab() ? "New project (Ctrl+T)" : "Maximum tabs reached"}
  ```

- **第 397 行**: `Scroll tabs right`
  ```typescript
  title="Scroll tabs right"
  ```

### src/components/TimelineNavigator.tsx (12 个文本)

- **第 93 行**: `Failed to load timeline`
  ```typescript
  setError("Failed to load timeline");
  ```

- **第 146 行**: `Failed to create checkpoint`
  ```typescript
  setError("Failed to create checkpoint");
  ```

- **第 186 行**: `Failed to restore checkpoint`
  ```typescript
  setError("Failed to restore checkpoint");
  ```

- **第 218 行**: `Failed to compare checkpoints`
  ```typescript
  setError("Failed to compare checkpoints");
  ```

- **第 310 行**: `No prompt`
  ```typescript
  {node.checkpoint.metadata.userPrompt || "No prompt"}
  ```

- **第 342 行**: `Restore to this checkpoint`
  ```typescript
  <TooltipContent>Restore to this checkpoint</TooltipContent>
  ```

- **第 361 行**: `Fork from this checkpoint`
  ```typescript
  <TooltipContent>Fork from this checkpoint</TooltipContent>
  ```

- **第 380 行**: `Compare with another checkpoint`
  ```typescript
  <TooltipContent>Compare with another checkpoint</TooltipContent>
  ```

- **第 462 行**: `No checkpoints yet`
  ```typescript
  {isLoading ? "Loading timeline..." : "No checkpoints yet"}
  ```

- **第 470 行**: `Create Checkpoint`
  ```typescript
  <DialogTitle>Create Checkpoint</DialogTitle>
  ```

- **第 485 行**: `Enter`
  ```typescript
  if (e.key === "Enter" && !isLoading) {
  ```

- **第 515 行**: `Checkpoint Comparison`
  ```typescript
  <DialogTitle>Checkpoint Comparison</DialogTitle>
  ```

### src/components/ToolWidgets.tsx (4 个文本)

- **第 518 行**: `File content`
  ```typescript
  {filePath || "File content"}
  ```

- **第 1226 行**: `The file`
  ```typescript
  if (line.includes('The file') && line.includes('has been updated')) {
  ```

- **第 2050 行**: `Task Instructions`
  ```typescript
  <span>Task Instructions</span>
  ```

- **第 2412 行**: `Analysis Prompt`
  ```typescript
  <span>Analysis Prompt</span>
  ```

### src/components/Topbar.tsx (4 个文本)

- **第 70 行**: `No such file or directory`
  ```typescript
  if (!status.is_installed && status.output.includes("No such file or directory")) {
  ```

- **第 78 行**: `Failed to check version`
  ```typescript
  output: "Failed to check version",
  ```

- **第 116 行**: `Claude Code`
  ```typescript
  : "Claude Code"}
  ```

- **第 148 行**: `Install Claude Code`
  ```typescript
  <span>Install Claude Code</span>
  ```

### src/components/UsageDashboard.original.tsx (2 个文本)

- **第 142 行**: `All Time`
  ```typescript
  {range === "all" ? "All Time" : range === "7d" ? "Last 7 Days" : "Last 30 Days"}
  ```

- **第 410 行**: `Daily Usage`
  ```typescript
  <span>Daily Usage</span>
  ```

### src/components/UsageDashboard.tsx (1 个文本)

- **第 647 行**: `Daily Usage`
  ```typescript
  <span>Daily Usage</span>
  ```

### src/components/WebviewPreview.tsx (6 个文本)

- **第 83 行**: `Escape`
  ```typescript
  if (e.key === 'Escape' && isMaximized && onToggleMaximize) {
  ```

- **第 135 行**: `Invalid URL`
  ```typescript
  setErrorMessage("Invalid URL");
  ```

- **第 146 行**: `Enter`
  ```typescript
  if (e.key === 'Enter') {
  ```

- **第 210 行**: `Enter full screen`
  ```typescript
  {isMaximized ? "Exit full screen (ESC)" : "Enter full screen"}
  ```

- **第 327 行**: `Preview`
  ```typescript
  title="Preview"
  ```

- **第 344 行**: `Try entering`
  ```typescript
  <span>Try entering</span>
  ```

### src/components/claude-code-session/MessageList.tsx (2 个文本)

- **第 84 行**: `Enter a prompt below to begin your Claude Code session`
  ```typescript
  ? "Enter a prompt below to begin your Claude Code session"
  ```

- **第 85 行**: `Select a project folder to begin`
  ```typescript
  : "Select a project folder to begin"}
  ```

### src/components/claude-code-session/PromptQueue.tsx (2 个文本)

- **第 65 行**: `Opus`
  ```typescript
  {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
  ```

- **第 65 行**: `Sonnet`
  ```typescript
  {queuedPrompt.model === "opus" ? "Opus" : "Sonnet"}
  ```

### src/components/ui/button.tsx (1 个文本)

- **第 63 行**: `Button`
  ```typescript
  Button.displayName = "Button";
  ```

### src/components/ui/card.tsx (6 个文本)

- **第 39 行**: `Card`
  ```typescript
  Card.displayName = "Card";
  ```

- **第 54 行**: `CardHeader`
  ```typescript
  CardHeader.displayName = "CardHeader";
  ```

- **第 69 行**: `CardTitle`
  ```typescript
  CardTitle.displayName = "CardTitle";
  ```

- **第 84 行**: `CardDescription`
  ```typescript
  CardDescription.displayName = "CardDescription";
  ```

- **第 95 行**: `CardContent`
  ```typescript
  CardContent.displayName = "CardContent";
  ```

- **第 110 行**: `CardFooter`
  ```typescript
  CardFooter.displayName = "CardFooter";
  ```

### src/components/ui/dialog.tsx (2 个文本)

- **第 65 行**: `DialogHeader`
  ```typescript
  DialogHeader.displayName = "DialogHeader"
  ```

- **第 79 行**: `DialogFooter`
  ```typescript
  DialogFooter.displayName = "DialogFooter"
  ```

### src/components/ui/dropdown-menu.tsx (1 个文本)

- **第 180 行**: `DropdownMenuShortcut`
  ```typescript
  DropdownMenuShortcut.displayName = "DropdownMenuShortcut"
  ```

### src/components/ui/input.tsx (1 个文本)

- **第 37 行**: `Input`
  ```typescript
  Input.displayName = "Input";
  ```

### src/components/ui/label.tsx (1 个文本)

- **第 26 行**: `Label`
  ```typescript
  Label.displayName = "Label";
  ```

### src/components/ui/popover.tsx (1 个文本)

- **第 86 行**: `Escape`
  ```typescript
  if (event.key === "Escape") {
  ```

### src/components/ui/scroll-area.tsx (1 个文本)

- **第 37 行**: `ScrollArea`
  ```typescript
  ScrollArea.displayName = "ScrollArea";
  ```

### src/components/ui/select.tsx (1 个文本)

- **第 194 行**: `Select an option`
  ```typescript
  placeholder = "Select an option",
  ```

### src/components/ui/split-pane.tsx (3 个文本)

- **第 133 行**: `ArrowLeft`
  ```typescript
  case 'ArrowLeft':
  ```

- **第 137 行**: `ArrowRight`
  ```typescript
  case 'ArrowRight':
  ```

- **第 141 行**: `Home`
  ```typescript
  case 'Home':
  ```

### src/components/ui/switch.tsx (1 个文本)

- **第 63 行**: `Switch`
  ```typescript
  Switch.displayName = "Switch";
  ```

### src/components/ui/tabs.tsx (3 个文本)

- **第 80 行**: `TabsList`
  ```typescript
  TabsList.displayName = "TabsList";
  ```

- **第 122 行**: `TabsTrigger`
  ```typescript
  TabsTrigger.displayName = "TabsTrigger";
  ```

- **第 155 行**: `TabsContent`
  ```typescript
  TabsContent.displayName = "TabsContent";
  ```

### src/components/ui/textarea.tsx (1 个文本)

- **第 21 行**: `Textarea`
  ```typescript
  Textarea.displayName = "Textarea"
  ```

### src/components/widgets/BashWidget.tsx (2 个文本)

- **第 65 行**: `Command failed`
  ```typescript
  {resultContent || (isError ? "Command failed" : "Command completed")}
  ```

- **第 65 行**: `Command completed`
  ```typescript
  {resultContent || (isError ? "Command failed" : "Command completed")}
  ```

### src/contexts/TabContext.tsx (1 个文本)

- **第 86 行**: `Projects`
  ```typescript
  title: 'Projects',
  ```

### src/lib/outputCache.tsx (1 个文本)

- **第 106 行**: `Failed to parse message`
  ```typescript
  error: 'Failed to parse message',
  ```

## 所有发现的文本列表

- API Key Helper Script
- Agent Preview
- AgentExecution
- All Files
- All Time
- Analysis Prompt
- Applied multiple edits to
- ArrowDown
- ArrowLeft
- ArrowRight
- ArrowUp
- Asterisk
- Available Agents
- BUILD TOOL
- Back to Agents
- Back to Projects
- Button
- CLAUDE CODE
- Card
- CardContent
- CardDescription
- CardFooter
- CardHeader
- CardTitle
- Checkpoint Comparison
- Checkpoint Settings
- Choose Claude installation
- Choose an icon
- Claude Code
- Claude Code Installation
- ClaudeCodeSession
- ClaudeSession
- Claudia
- Claudia Agent
- Click to select
- Collapse queue
- Command
- Command completed
- Command failed
- Commands
- Communication
- Compare with another checkpoint
- Completed
- Copy conversation
- Create Checkpoint
- Custom
- Customizes notifications when Claude needs attention
- Daily Usage
- Deeper analysis
- Default
- Delete Agent
- Delete Row
- DialogFooter
- DialogHeader
- DropdownMenuShortcut
- Edit
- Edit Row
- Empty directory
- Enable Analytics
- Enable Proxy
- Enter
- Enter a name for the forked session
- Enter a prompt below to begin your Claude Code session
- Enter full screen
- Enter fullscreen
- Error loading installations
- Escape
- Example Commands
- Execution stopped by user
- Exit fullscreen
- Expand queue
- Explain how something works
- Extensive reasoning
- External URL
- Failed
- Failed to check version
- Failed to compare checkpoints
- Failed to create checkpoint
- Failed to fork checkpoint
- Failed to load Claude installations
- Failed to load commands
- Failed to load directory
- Failed to load proxy settings
- Failed to load running sessions
- Failed to load session history
- Failed to load timeline
- Failed to open folder picker
- Failed to parse message
- Failed to restore checkpoint
- Failed to save Claude binary path
- Failed to save proxy settings
- Failed to send prompt
- File a bug
- File content
- Fix a specific issue
- FloatingPromptInput
- Fork Session
- Fork Session from Checkpoint
- Fork from this checkpoint
- Framer Motion
- Fullscreen
- Go Back
- Grep
- HTTP Proxy
- HTTPS Proxy
- Home
- Input
- Install Claude Code
- Invalid URL
- JSON Files
- JSON Format Examples
- JSONL Viewer Model Configuration and Setup
- Label
- Local Development Server
- MCP PROTOCOL
- Maximum tabs reached
- Minimize
- Miscellaneous
- Model Context Protocol
- MultiEdit
- MultiEdit completed successfully
- New Row
- New Session
- New Session Name
- No Proxy
- No checkpoints yet
- No commands found
- No custom commands available
- No default commands available
- No files found
- No output available yet
- No prompt
- No such file or directory
- Notification
- Opus
- PACKAGE MANAGER
- POWERED BY
- Pattern
- Pending
- Please select a project directory first
- Post Tool Use
- PostToolUse
- Pre Tool Use
- PreToolUse
- Preview
- Project Commands
- Projects
- Read
- Refresh output
- Remember Open Tabs
- Reset Database
- Restore to this checkpoint
- Review code for best practices
- Running
- Runs after successful tool completion
- Runs when Claude finishes responding
- SQL Query
- SQL Query Editor
- Save Selection
- Scope
- Scroll tabs left
- Scroll tabs right
- Scroll to bottom
- Scroll to top
- ScrollArea
- Search failed
- Segoe UI
- Select Claude installation
- Select Project Directory
- Select Project Folder
- Select a project folder to begin
- Select an option
- Send message
- Server Name
- Session Timeline
- Session cancelled by user
- SessionCard
- Show Welcome Intro on Startup
- Slash Commands
- Sonnet
- Stop
- Stop execution
- Stop generation
- Subagent Stop
- SubagentStop
- Switch
- System
- TabsContent
- TabsList
- TabsTrigger
- Task Instructions
- Tauri Framework
- Textarea
- The Ultimate Coding Assistant
- The file
- Theme
- Think Harder
- To all the beta testers
- To everyone who believed in this project
- To the open source community
- Tool execution failed
- Try entering
- UI FRAMEWORK
- Unknown
- Unknown error
- Unknown time
- Unknown version
- UnknownError
- Unsaved changes
- User Commands
- Verbose Output
- Version unknown
- Vite
- WebSearch
- Welcome intro disabled
- Welcome intro enabled
- Write
- Write tests for code

## 建议的翻译键结构

```json
{
  "errors": {
    "failedToCheckVersion": "Failed to check version",
    "failedToLoadTimeline": "Failed to load timeline",
    "failedToOpenFolderPicker": "Failed to open folder picker",
    "failedToCompareCheckpoints": "Failed to compare checkpoints",
    "errorLoadingInstallations": "Error loading installations",
    "failedToParseMessage": "Failed to parse message",
    "unknownError": "Unknown error",
    "failed": "Failed",
    "failedToSaveProxySettings": "Failed to save proxy settings",
    "commandFailed": "Command failed",
    "failedToRestoreCheckpoint": "Failed to restore checkpoint",
    "failedToLoadRunningSessions": "Failed to load running sessions",
    "failedToForkCheckpoint": "Failed to fork checkpoint",
    "failedToLoadClaudeInstallations": "Failed to load Claude installations",
    "toolExecutionFailed": "Tool execution failed",
    "failedToLoadDirectory": "Failed to load directory",
    "failedToSendPrompt": "Failed to send prompt",
    "failedToCreateCheckpoint": "Failed to create checkpoint",
    "failedToLoadProxySettings": "Failed to load proxy settings",
    "failedToLoadSessionHistory": "Failed to load session history",
    "failedToLoadCommands": "Failed to load commands",
    "unknownerror": "UnknownError",
    "searchFailed": "Search failed",
    "failedToSaveClaudeBinaryPath": "Failed to save Claude binary path",
  },
  "success": {
    "commandCompleted": "Command completed",
    "completed": "Completed",
    "unsavedChanges": "Unsaved changes",
    "multieditCompletedSuccessfully": "MultiEdit completed successfully",
    "runsAfterSuccessfulToolCompletion": "Runs after successful tool completion",
  },
  "ui": {
    "chooseAnIcon": "Choose an icon",
    "selectAProjectFolderToBegin": "Select a project folder to begin",
    "selectProjectFolder": "Select Project Folder",
    "clickToSelect": "Click to select",
    "enterFullScreen": "Enter full screen",
    "enter": "Enter",
    "enterANameForTheForkedSession": "Enter a name for the forked session",
    "enterFullscreen": "Enter fullscreen",
    "selectClaudeInstallation": "Select Claude installation",
    "tryEntering": "Try entering",
    "pleaseSelectAProjectDirectoryFirst": "Please select a project directory first",
    "saveSelection": "Save Selection",
    "chooseClaudeInstallation": "Choose Claude installation",
    "selectAnOption": "Select an option",
    "enterAPromptBelowToBeginYourClaudeCodeSession": "Enter a prompt below to begin your Claude Code session",
    "selectProjectDirectory": "Select Project Directory",
  },
  "actions": {
    "deleteRow": "Delete Row",
    "deleteAgent": "Delete Agent",
    "createCheckpoint": "Create Checkpoint",
  },
  "status": {
    "pending": "Pending",
    "executionStoppedByUser": "Execution stopped by user",
    "running": "Running",
  },
  "misc": {
    "system": "System",
    "pattern": "Pattern",
    "fileABug": "File a bug",
    "newRow": "New Row",
    "tabslist": "TabsList",
    "backToAgents": "Back to Agents",
    "localDevelopmentServer": "Local Development Server",
    "claudia": "Claudia",
    "fileContent": "File content",
    "enableAnalytics": "Enable Analytics",
    "sqlQuery": "SQL Query",
    "unknown": "Unknown",
    "preview": "Preview",
    "copyConversation": "Copy conversation",
    "jsonFormatExamples": "JSON Format Examples",
    "toEveryoneWhoBelievedInThisProject": "To everyone who believed in this project",
    "arrowright": "ArrowRight",
    "reviewCodeForBestPractices": "Review code for best practices",
    "allFiles": "All Files",
    "jsonlViewerModelConfigurationAndSetup": "JSONL Viewer Model Configuration and Setup",
    "command": "Command",
    "allTime": "All Time",
    "editRow": "Edit Row",
    "vite": "Vite",
    "stopGeneration": "Stop generation",
    "floatingpromptinput": "FloatingPromptInput",
    "toTheOpenSourceCommunity": "To the open source community",
    "scrollToBottom": "Scroll to bottom",
    "unknownVersion": "Unknown version",
    "resetDatabase": "Reset Database",
    "button": "Button",
    "analysisPrompt": "Analysis Prompt",
    "arrowdown": "ArrowDown",
    "dialogheader": "DialogHeader",
    "dailyUsage": "Daily Usage",
    "userCommands": "User Commands",
    "projectCommands": "Project Commands",
    "noCheckpointsYet": "No checkpoints yet",
    "sessionTimeline": "Session Timeline",
    "arrowup": "ArrowUp",
    "versionUnknown": "Version unknown",
    "noFilesFound": "No files found",
    "agentexecution": "AgentExecution",
    "showWelcomeIntroOnStartup": "Show Welcome Intro on Startup",
    "write": "Write",
    "exitFullscreen": "Exit fullscreen",
    "opus": "Opus",
    "httpsProxy": "HTTPS Proxy",
    "postToolUse": "Post Tool Use",
    "theme": "Theme",
    "taskInstructions": "Task Instructions",
    "extensiveReasoning": "Extensive reasoning",
    "externalUrl": "External URL",
    "noPrompt": "No prompt",
    "restoreToThisCheckpoint": "Restore to this checkpoint",
    "cardcontent": "CardContent",
    "dropdownmenushortcut": "DropdownMenuShortcut",
    "apiKeyHelperScript": "API Key Helper Script",
    "enableProxy": "Enable Proxy",
    "claudeCodeInstallation": "Claude Code Installation",
    "exampleCommands": "Example Commands",
    "runsWhenClaudeFinishesResponding": "Runs when Claude finishes responding",
    "sessionCancelledByUser": "Session cancelled by user",
    "sqlQueryEditor": "SQL Query Editor",
    "websearch": "WebSearch",
    "custom": "Custom",
    "claudesession": "ClaudeSession",
    "availableAgents": "Available Agents",
    "sendMessage": "Send message",
    "verboseOutput": "Verbose Output",
    "card": "Card",
    "buildTool": "BUILD TOOL",
    "invalidUrl": "Invalid URL",
    "tauriFramework": "Tauri Framework",
    "claudecodesession": "ClaudeCodeSession",
    "explainHowSomethingWorks": "Explain how something works",
    "fullscreen": "Fullscreen",
    "slashCommands": "Slash Commands",
    "sessioncard": "SessionCard",
    "scrollTabsLeft": "Scroll tabs left",
    "miscellaneous": "Miscellaneous",
    "forkFromThisCheckpoint": "Fork from this checkpoint",
    "noCommandsFound": "No commands found",
    "label": "Label",
    "home": "Home",
    "appliedMultipleEditsTo": "Applied multiple edits to",
    "refreshOutput": "Refresh output",
    "read": "Read",
    "checkpointComparison": "Checkpoint Comparison",
    "unknownTime": "Unknown time",
    "subagentStop": "Subagent Stop",
    "posttooluse": "PostToolUse",
    "scrollToTop": "Scroll to top",
    "welcomeIntroDisabled": "Welcome intro disabled",
    "serverName": "Server Name",
    "customizesNotificationsWhenClaudeNeedsAttention": "Customizes notifications when Claude needs attention",
    "modelContextProtocol": "Model Context Protocol",
    "goBack": "Go Back",
    "preToolUse": "Pre Tool Use",
    "input": "Input",
    "noProxy": "No Proxy",
    "switch": "Switch",
    "subagentstop": "SubagentStop",
    "minimize": "Minimize",
    "cardheader": "CardHeader",
    "rememberOpenTabs": "Remember Open Tabs",
    "framerMotion": "Framer Motion",
    "escape": "Escape",
    "claudiaAgent": "Claudia Agent",
    "arrowleft": "ArrowLeft",
    "theUltimateCodingAssistant": "The Ultimate Coding Assistant",
    "collapseQueue": "Collapse queue",
    "noCustomCommandsAvailable": "No custom commands available",
    "maximumTabsReached": "Maximum tabs reached",
    "forkSession": "Fork Session",
    "scrollTabsRight": "Scroll tabs right",
    "edit": "Edit",
    "newSessionName": "New Session Name",
    "toAllTheBetaTesters": "To all the beta testers",
    "expandQueue": "Expand queue",
    "poweredBy": "POWERED BY",
    "welcomeIntroEnabled": "Welcome intro enabled",
    "dialogfooter": "DialogFooter",
    "tabscontent": "TabsContent",
    "noOutputAvailableYet": "No output available yet",
    "noSuchFileOrDirectory": "No such file or directory",
    "cardfooter": "CardFooter",
    "claudeCode": "CLAUDE CODE",
    "segoeUi": "Segoe UI",
    "projects": "Projects",
    "theFile": "The file",
    "packageManager": "PACKAGE MANAGER",
    "textarea": "Textarea",
    "installClaudeCode": "Install Claude Code",
    "newSession": "New Session",
    "claudeCode": "Claude Code",
    "scope": "Scope",
    "backToProjects": "Back to Projects",
    "jsonFiles": "JSON Files",
    "asterisk": "Asterisk",
    "uiFramework": "UI FRAMEWORK",
    "scrollarea": "ScrollArea",
    "commands": "Commands",
    "emptyDirectory": "Empty directory",
    "checkpointSettings": "Checkpoint Settings",
    "deeperAnalysis": "Deeper analysis",
    "fixASpecificIssue": "Fix a specific issue",
    "stopExecution": "Stop execution",
    "thinkHarder": "Think Harder",
    "noDefaultCommandsAvailable": "No default commands available",
    "writeTestsForCode": "Write tests for code",
    "agentPreview": "Agent Preview",
    "grep": "Grep",
    "forkSessionFromCheckpoint": "Fork Session from Checkpoint",
    "communication": "Communication",
    "notification": "Notification",
    "stop": "Stop",
    "multiedit": "MultiEdit",
    "cardtitle": "CardTitle",
    "mcpProtocol": "MCP PROTOCOL",
    "default": "Default",
    "sonnet": "Sonnet",
    "httpProxy": "HTTP Proxy",
    "pretooluse": "PreToolUse",
    "compareWithAnotherCheckpoint": "Compare with another checkpoint",
    "carddescription": "CardDescription",
    "tabstrigger": "TabsTrigger",
  },
}
```